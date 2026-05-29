import math

class AlphaBeta:
    def __init__(self, max_depth, heuristic):
        self.max_depth = max_depth
        self.heuristic = heuristic
        self.nodes = 0
    
    def search(self, board, ai_player, human_player):
        self.nodes = 0
        _, best_move = self._alpha_beta(board, self.max_depth, -math.inf, math.inf, True, ai_player, human_player, None, None)
        return best_move, self.nodes
    
    def _alpha_beta(self, board, depth, alpha, beta, is_max, ai_player, human_player, last_row, last_col):
        self.nodes += 1
        
        from game.rules import Rules
        rules = Rules()
        
        if last_row is not None:
            last_player = ai_player if not is_max else human_player
            if rules.check_win(board, last_row, last_col, last_player):
                if last_player == ai_player:
                    return (1000000 + depth, None)
                else:
                    return (-1000000 - depth, None)
        
        if depth == 0:
            return (self.heuristic.evaluate(board, ai_player, human_player), None)
        
        from game.move_generator import MoveGenerator
        moves = MoveGenerator.get_moves(board)
        
        if len(moves) == 0:
            return (0, None)
        
        center = board.size // 2
        moves.sort(key=lambda pos: (pos[0] - center)**2 + (pos[1] - center)**2)
        
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
            return (best_value, best_move)
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
            return (best_value, best_move)