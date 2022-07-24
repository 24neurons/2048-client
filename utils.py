"""
    maximizer and minimizer according to minimax tree
"""

from Grid import Grid

def Maximizer(gr: Grid, depth: int): 
    """
        maximizer according to minimax tree"""
    score = -1

    ans = ["NULL", gr.Optimizer_score()]

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


def Minimizer(gr: Grid, depth: int): #pylint: disable=invalid-name
    """
        minimizer according to minimax tree
    """
    score = 10000000000000000

    if depth == 0:
        return gr.Optimizer_score()

    else:
        Possible_grids = gr.addRandomcell()

        if len(Possible_grids) == 0:
            return gr.Optimizer_score()

        for x in Possible_grids:
            current_score = Maximizer(x, depth - 1)[1]

            if current_score < score:
                score = current_score

        return score
