import math
import time

class AlphaBeta:
    def __init__(self, max_depth, heuristic, time_budget=5.0):
        self.max_depth = max_depth
        self.heuristic = heuristic
        self.time_budget = time_budget
        self.nodes = 0
        self.start_time = 0
        self.cache = {}
    
    def _quick_score(self, board, row, col, ai_player, human_player):
        """Tính điểm nhanh cho 1 nước đi (dùng để sắp xếp)"""
        size = board.size
        directions = [(1,0), (0,1), (1,1), (1,-1)]
        
        def count_dir(r, c, dr, dc, player):
            cnt = 0
            nr, nc = r, c
            while 0 <= nr < size and 0 <= nc < size and board.get(nr, nc) == player:
                cnt += 1
                nr += dr
                nc += dc
            return cnt
        
        attack_score = 0
        for dr, dc in directions:
            cnt = count_dir(row, col, dr, dc, ai_player)
            if cnt >= 4:
                attack_score += 1000000
            elif cnt == 3:
                attack_score += 5000
            elif cnt == 2:
                attack_score += 100
        
        defend_score = 0
        for dr, dc in directions:
            cnt = count_dir(row, col, dr, dc, human_player)
            if cnt >= 4:
                defend_score += 1000000
            elif cnt == 3:
                defend_score += 8000
            elif cnt == 2:
                defend_score += 200
        
        return attack_score * 2 + defend_score
    
    def _order_moves(self, board, moves, ai_player, human_player):
        """Sắp xếp nước đi theo thứ tự ưu tiên (move ordering)"""
        if not moves:
            return moves
        
        scored = []
        for r, c in moves:
            score = self._quick_score(board, r, c, ai_player, human_player)
            scored.append((score, (r, c)))
        scored.sort(key=lambda x: x[0], reverse=True)
        return [move for _, move in scored]
    
    def _hash_board(self, board):
        """Tạo hash đơn giản cho bàn cờ (dùng cache)"""
        return hash(''.join([''.join(row) for row in board.grid]))
    
    def search(self, board, ai_player, human_player):
        """Tìm nước đi tốt nhất với iterative deepening + time budget + cache"""
        self.start_time = time.time()
        self.cache.clear()
        best_move = None
        best_value = -math.inf
        
        moves = self._order_moves(board, self._get_moves(board), ai_player, human_player)
        if not moves:
            return None, 0
        
        for depth in range(1, self.max_depth + 1):
            if time.time() - self.start_time > self.time_budget:
                break
            
            self.nodes = 0
            value, move = self._alpha_beta(board, depth, -math.inf, math.inf, True, ai_player, human_player, None, None)
            
            if move is not None:
                best_move = move
                best_value = value
        
        return best_move, self.nodes
    
    def _get_moves(self, board):
        from game.move_generator import MoveGenerator
        return MoveGenerator.get_moves(board)
    
    def _alpha_beta(self, board, depth, alpha, beta, is_max, ai_player, human_player, last_row, last_col):
        self.nodes += 1
        
        # Timeout check
        if time.time() - self.start_time > self.time_budget:
            return (0, None)
        
        # Cache check
        board_hash = self._hash_board(board)
        cache_key = (board_hash, depth, is_max)
        if cache_key in self.cache:
            return self.cache[cache_key]
        
        from game.rules import Rules
        rules = Rules()
        
        if last_row is not None:
            last_player = ai_player if not is_max else human_player
            if rules.check_win(board, last_row, last_col, last_player):
                result = (1000000 + depth, None) if last_player == ai_player else (-1000000 - depth, None)
                self.cache[cache_key] = result
                return result
        
        if depth == 0:
            val = self.heuristic.evaluate(board, ai_player, human_player)
            result = (val, None)
            self.cache[cache_key] = result
            return result
        
        moves = self._get_moves(board)
        if not moves:
            result = (0, None)
            self.cache[cache_key] = result
            return result
        
        # Move ordering mạnh hơn
        moves = self._order_moves(board, moves, ai_player, human_player)
        
        if is_max:
            best_value = -math.inf
            best_move = moves[0]
            for move in moves:
                r, c = move
                new_board = board.clone()
                new_board.set(r, c, ai_player)
                value, _ = self._alpha_beta(new_board, depth - 1, alpha, beta, False, ai_player, human_player, r, c)
                if value > best_value:
                    best_value = value
                    best_move = move
                alpha = max(alpha, best_value)
                if beta <= alpha:
                    break
            result = (best_value, best_move)
            self.cache[cache_key] = result
            return result
        else:
            best_value = math.inf
            best_move = moves[0]
            for move in moves:
                r, c = move
                new_board = board.clone()
                new_board.set(r, c, human_player)
                value, _ = self._alpha_beta(new_board, depth - 1, alpha, beta, True, ai_player, human_player, r, c)
                if value < best_value:
                    best_value = value
                    best_move = move
                beta = min(beta, best_value)
                if beta <= alpha:
                    break
            result = (best_value, best_move)
            self.cache[cache_key] = result
            return result