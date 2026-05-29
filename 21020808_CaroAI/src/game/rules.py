class Rules:
    @staticmethod
    def check_win(board, row, col, player):
        size = board.size
        directions = [(1, 0), (0, 1), (1, 1), (1, -1)]
        
        for dr, dc in directions:
            count = 1
            
            r, c = row + dr, col + dc
            while 0 <= r < size and 0 <= c < size and board.get(r, c) == player:
                count += 1
                r += dr
                c += dc
            
            r, c = row - dr, col - dc
            while 0 <= r < size and 0 <= c < size and board.get(r, c) == player:
                count += 1
                r -= dr
                c -= dc
            
            if count >= 4:
                return True
        return False
    
    @staticmethod
    def is_draw(board):
        return board.is_full()
    