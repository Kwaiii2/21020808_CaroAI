class Heuristic:
    @staticmethod
    def evaluate(board, ai_player='O', human_player='X'):
        size = board.size
        directions = [(1, 0), (0, 1), (1, 1), (1, -1)]
        
        def count_consecutive(r, c, dr, dc, player):
            cnt = 0
            nr, nc = r, c
            while 0 <= nr < size and 0 <= nc < size and board.get(nr, nc) == player:
                cnt += 1
                nr += dr
                nc += dc
            return cnt
        
        def check_open_three(r, c, dr, dc, player):
            """Kiểm tra chuỗi 3 có 2 đầu mở không"""
            cnt = 0
            nr, nc = r, c
            while 0 <= nr < size and 0 <= nc < size and board.get(nr, nc) == player:
                cnt += 1
                nr += dr
                nc += dc
            # Kiểm tra đầu mở
            open_end = 0
            if 0 <= nr < size and 0 <= nc < size and board.get(nr, nc) == '.':
                open_end += 1
            nr, nc = r - dr, c - dc
            while 0 <= nr < size and 0 <= nc < size and board.get(nr, nc) == player:
                nr -= dr
                nc -= dc
            if 0 <= nr < size and 0 <= nc < size and board.get(nr, nc) == '.':
                open_end += 1
            return cnt, open_end
        
        def score_for_player(player, is_human=False):
            total = 0
            for r in range(size):
                for c in range(size):
                    if board.get(r, c) == player:
                        for dr, dc in directions:
                            cnt, open_end = check_open_three(r, c, dr, dc, player)
                            if cnt >= 4:
                                total += 1000000
                            elif cnt == 3:
                                if is_human:
                                    total += 20000  # Chặn người ưu tiên cao hơn
                                else:
                                    total += 10000
                            elif cnt == 2 and open_end >= 1:
                                total += 500
                            elif cnt == 1:
                                total += 1
            return total
        
        ai_score = score_for_player(ai_player, is_human=False)
        human_score = score_for_player(human_player, is_human=True)
        
        return ai_score - human_score * 1.5