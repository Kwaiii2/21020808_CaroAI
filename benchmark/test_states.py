from game.board import Board

class TestStates:
    @staticmethod
    def state_1():
        board = Board(10)
        return board
    
    @staticmethod
    def state_2():
        board = Board(10)
        board.set(4, 4, 'X')
        board.set(4, 5, 'O')
        board.set(5, 4, 'O')
        board.set(5, 5, 'X')
        return board
    
    @staticmethod
    def state_3():
        board = Board(10)
        board.set(5, 2, 'O')
        board.set(5, 3, 'O')
        board.set(5, 4, 'O')
        return board
    
    @staticmethod
    def state_4():
        board = Board(10)
        board.set(3, 5, 'X')
        board.set(4, 5, 'X')
        board.set(5, 5, 'X')
        return board
    
    @staticmethod
    def state_5():
        board = Board(10)
        moves = [(3,3,'X'), (3,4,'O'), (4,3,'O'), (4,4,'X'),
                 (5,5,'X'), (5,6,'O'), (6,5,'O'), (6,6,'X')]
        for r,c,p in moves:
            board.set(r, c, p)
        return board
    
    @staticmethod
    def get_all():
        return [
            ("Dau van", TestStates.state_1()),
            ("Giua van", TestStates.state_2()),
            ("May thang ngay", TestStates.state_3()),
            ("Nguoi sap thang", TestStates.state_4()),
            ("The roi", TestStates.state_5())
        ]