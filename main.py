from Grid import Grid
from GameDriver import GameDriver
from utils import Maximizer
import argparse

gameDriver = GameDriver()
moves_str = ['UP', 'DOWN', 'LEFT', 'RIGHT']
moves_count = 1


def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument('--heuristic_function', type=str, default='greedy', help='Heuristic function to calculate next move',
                        choices=['greedy', 'empty' , 'monocity', 'uniformity', 'monotocity', 'smoothness', 'max_tile'])
    args = parser.parse_args()
    return args
def main():
    args = parse_arguments()
    while True:
        grid = gameDriver.getGrid()
        moveCode = Maximizer(grid, 5)[0]
        
        #if the game is over
        if moveCode == 'NULL':
            print(f'Game over! Your score is {grid.Optimizer_score()}')
            break
        print(f'Move #{moves_count}: {moves_str[moveCode]}')
        gameDriver.move(moveCode)
        moves_count += 1

    

if __name__ == '__main__':
    main()