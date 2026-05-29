import time
from src.ai.minimax import Minimax
from src.ai.alpha_beta import AlphaBeta
from src.ai.heuristic import Heuristic

class Comparator:
    def __init__(self, max_depth):
        self.max_depth = max_depth
        self.heuristic = Heuristic()
    
    def compare(self, board, ai_player='O', human_player='X'):
        minimax_agent = Minimax(self.max_depth, self.heuristic)
        start = time.time()
        move_mm, nodes_mm = minimax_agent.search(board, ai_player, human_player)
        time_mm = (time.time() - start) * 1000
        
        ab_agent = AlphaBeta(self.max_depth, self.heuristic)
        start = time.time()
        move_ab, nodes_ab = ab_agent.search(board, ai_player, human_player)
        time_ab = (time.time() - start) * 1000
        
        reduction = 0
        if nodes_mm > 0:
            reduction = (1 - nodes_ab / nodes_mm) * 100
        
        return {
            'minimax': {'move': move_mm, 'nodes': nodes_mm, 'time_ms': time_mm},
            'alpha_beta': {'move': move_ab, 'nodes': nodes_ab, 'time_ms': time_ab},
            'reduction': reduction
        }