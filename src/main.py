from Grid import Grid
from GameDriver import GameDriver
from utils import Maximizer, Heuristic
import argparse

gameDriver = GameDriver()
moves_str = ['UP', 'DOWN', 'LEFT', 'RIGHT']

def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument('--heuristic_function', type=str, default='greedy', help='Heuristic function to calculate next move',
                        choices=['greedy', 'empty' , 'monocity', 'uniformity', 'monotocity', 'smoothness', 'max_tile'])
    parser.add_argument('--browser', type=str, default='Chrome', help="Browser to run the game",
                        choices=["Chrome", "Firefox"])
    args = parser.parse_args()
    return args

def main():
    args = parse_arguments()
    moves_count = 1
    while True:
        grid = gameDriver.getGrid()

        grid.Intro()

        moveCode = Maximizer(grid, 5, args.heuristic_function)[0]
        
        #if the game is over
        if moveCode == 'NULL':
            print(f'Game over! Your score is {Heuristic(grid, args.heuristic_function)}')
            break
        print(f'Move #{moves_count}: {moves_str[moveCode]}')
        gameDriver.move(moveCode)
        moves_count += 1

    

if __name__ == '__main__':
    main()