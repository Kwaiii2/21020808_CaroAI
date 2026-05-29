import copy

class Board:
    def __init__(self, size=10):
        self.size = size
        self.grid = [['.' for _ in range(size)] for _ in range(size)]
    
    def get(self, row, col):
        return self.grid[row][col]
    
    def set(self, row, col, player):
        self.grid[row][col] = player
    
    def is_empty(self, row, col):
        return self.grid[row][col] == '.'
    
    def clone(self):
        new_board = Board(self.size)
        new_board.grid = copy.deepcopy(self.grid)
        return new_board
    
    def get_all_empty(self):
        moves = []
        for r in range(self.size):
            for c in range(self.size):
                if self.grid[r][c] == '.':
                    moves.append((r, c))
        return moves
    
    def is_full(self):
        for r in range(self.size):
            for c in range(self.size):
                if self.grid[r][c] == '.':
                    return False
        return True