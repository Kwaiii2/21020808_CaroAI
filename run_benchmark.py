from benchmark.test_states import TestStates
from benchmark.comparator import Comparator
import config

def main():
    print("=" * 70)
    print("BENCHMARK: Minimax vs Alpha-Beta")
    print(f"Do sau: {config.MAX_DEPTH}")
    print("=" * 70)
    
    comparator = Comparator(config.MAX_DEPTH)
    test_cases = TestStates.get_all()
    
    for name, board in test_cases:
        print(f"\n{name}")
        result = comparator.compare(board)
        
        mm = result['minimax']
        ab = result['alpha_beta']
        
        print(f"  Minimax    : nuoc {mm['move']}, nodes={mm['nodes']}, time={mm['time_ms']:.2f}ms")
        print(f"  Alpha-Beta : nuoc {ab['move']}, nodes={ab['nodes']}, time={ab['time_ms']:.2f}ms")
        print(f"  Giam {result['reduction']:.1f}% so node")
        
        if mm['move'] == ab['move']:
            print("  => Cung nuoc di")
        else:
            print("  => Khac nuoc di")

if __name__ == "__main__":
    main()