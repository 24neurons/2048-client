"""
    maximizer and minimizer according to minimax tree
"""

from Grid import Grid
import argparse

def Maximizer(gr: Grid, depth: int, heuristic_function : str): 
    """
        maximizer according to minimax tree
        Args:
            gr (Grid): current grid
            depth (int): depth of the tree
            heuristic_function (str): heuristic function to calculate next move
        Returns:
            list: [move, score] : List of the best moves for maximizer and their scores
    """
    score = -1

    ans = ["NULL", Heuristic(gr, heuristic_function=heuristic_function)]

    if depth == 0:
        return ans
    else:
        possible_moves = gr.getPossibleMaximizerMoves()

        if len(possible_moves) == 0:
            return ans
        for x in possible_moves:
            current_score = Minimizer(x[1], depth - 1)

            if current_score > score:
                score = current_score
                ans = [x[0], score]
            
        return ans 


def Minimizer(gr: Grid, depth: int, heuristic_function : str): #pylint: disable=invalid-name
    """
        minimizer according to minimax tree
        Args:
            gr (Grid): current grid
            depth (int): depth of the tree
            heuristic_function (str): heuristic function to calculate next move
        Returns:
            int: score : score of the best move for minimizer

    """
    score = 10000000000000000

    if depth == 0:
        return Heuristic(gr, heuristic_function=heuristic_function)

    else:
        Possible_grids = gr.addRandomcell()

        if len(Possible_grids) == 0:
            return Heuristic(gr, heuristic_function=heuristic_function)

        for x in Possible_grids:
            current_score = Maximizer(x, depth - 1)[1]

            if current_score < score:
                score = current_score

        return score

def Heuristic(gr: Grid, heuristic_function: str):
    """
        Heuristic function to calculate next move
    """
    if heuristic_function == 'greedy':
        return gr.Optimizer_score()
    elif heuristic_function == 'empty':
        return gr.getEmptyCells()
    elif heuristic_function == 'uniformity':
        return gr.getUniformity()
    elif heuristic_function == 'monotocity':
        return gr.getMonotocity()
    elif heuristic_function == 'smoothness':
        return gr.getSmoothness()
    elif heuristic_function == 'max_tile':
        return gr.getMaxTile()
    else:
        raise ValueError('Invalid heuristic function')