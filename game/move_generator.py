class MoveGenerator:
    @staticmethod
    def get_moves(board):
        size = board.size
        
        occupied = []
        for r in range(size):
            for c in range(size):
                if board.get(r, c) != '.':
                    occupied.append((r, c))
        
        if len(occupied) == 0:
            center = size // 2
            return [(center, center)]
        
        candidates = set()
        for r, c in occupied:
            for dr in range(-2, 3):
                for dc in range(-2, 3):
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < size and 0 <= nc < size and board.is_empty(nr, nc):
                        candidates.add((nr, nc))
        
        if len(candidates) == 0:
            return board.get_all_empty()
        
        center = size // 2
        moves = list(candidates)
        moves.sort(key=lambda pos: (pos[0] - center)**2 + (pos[1] - center)**2)
        
        return moves    