import time
from game.board import Board
from game.rules import Rules
from ai.heuristic import Heuristic
from ai.minimax import Minimax
from ai.alpha_beta import AlphaBeta
from ui.console import ConsoleUI
import config

def main():
    ui = ConsoleUI()
    board = Board(config.BOARD_SIZE)
    rules = Rules()
    heuristic = Heuristic()
    
    print("=" * 50)
    print("Caro AI - 4 quan thang")
    print(f"Ban co {config.BOARD_SIZE}x{config.BOARD_SIZE}")
    print(f"Do sau: {config.MAX_DEPTH}")
    print("1. Minimax")
    print("2. Alpha-Beta")
    choice = input("Chon: ")
    algo = 'minimax' if choice == '1' else 'alpha_beta'
    print("=" * 50)
    
    ui.display(board)
    
    human_turn = True
    
    while True:
        if human_turn:
            print("\nLuot ban (X):")
            row, col = ui.get_human_move(board)
            board.set(row, col, 'X')
            ui.display(board)
            
            if rules.check_win(board, row, col, 'X'):
                print("BAN THANG!")
                break
            if rules.is_draw(board):
                print("HOA!")
                break
            human_turn = False
        
        else:
            print("\nLuot may (O):")
            
            if algo == 'minimax':
                agent = Minimax(config.MAX_DEPTH, heuristic, time_budget=config.TIME_BUDGET)
                start = time.time()
                move, nodes = agent.search(board, 'O', 'X')
                elapsed = (time.time() - start) * 1000
                value, _ = agent._minimax(board, config.MAX_DEPTH, True, 'O', 'X', None, None)
            else:
                agent = AlphaBeta(config.MAX_DEPTH, heuristic, time_budget=config.TIME_BUDGET)
                start = time.time()
                move, nodes = agent.search(board, 'O', 'X')
                elapsed = (time.time() - start) * 1000
                value, _ = agent._alpha_beta(board, config.MAX_DEPTH, -float('inf'), float('inf'), True, 'O', 'X', None, None)
            
            if move:
                board.set(move[0], move[1], 'O')
                ui.show_ai_move(move, value, nodes, elapsed, config.MAX_DEPTH, algo)
                ui.display(board)
                
                if rules.check_win(board, move[0], move[1], 'O'):
                    print("MAY THANG!")
                    break
                if rules.is_draw(board):
                    print("HOA!")
                    break
            
            human_turn = True

if __name__ == "__main__":
    main()
    