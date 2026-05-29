class ConsoleUI:
    @staticmethod
    def display(board):
        size = board.size
        print("\n  " + " ".join(str(i) for i in range(size)))
        for i in range(size):
            row = [board.get(i, j) for j in range(size)]
            print(f"{i} " + " ".join(row))
        print()
    
    @staticmethod
    def get_human_move(board):
        while True:
            try:
                row = int(input("Hang: "))
                col = int(input("Cot: "))
                if board.is_empty(row, col):
                    return (row, col)
                else:
                    print("O da co quan!")
            except (ValueError, IndexError):
                print("Nhap so tu 0 den 9")
    
    @staticmethod
    def show_ai_move(move, value, nodes, time_ms, depth, algo_name):
        print(f"\nAI ({algo_name}) chon: ({move[0]}, {move[1]})")
        print(f"  Gia tri: {value:.2f}")
        print(f"  Do sau: {depth}")
        print(f"  So trang thai: {nodes}")
        print(f"  Thoi gian: {time_ms:.2f} ms")