# 2048-client

A Python implemtation of a heuristic-based algorithm called expectimax to play the game [2048](https://play2048.co/)


## Set-up

This is just a module intended to implement the minimax algorithm to interact temporarily with the server

## Usage 

1. Clone the repository 
` git clone https://github.com/24neurons/2048-client `

2. Install the requirements 
` pip install -r requirements.txt `
3. Run the script 
`cd src`
` python main.py --heuristic_function <heuristic_function>` --browser <browser>`
with heuristic functions in the list of
`['greedy', 'empty', 'max_tile_weighted_smoothness', 'max_tile_weighted_smoothness_monotonicity']` 

browser can be either `chrome` or `firefox`

Example: 
`python main.py --heuristic_function greedy --browser chrome`

## To-do list
1. Add more heuristics
2. Add depth argument

## References

1. [2048](https://play2048.co/)
2. [Expectimax](https://en.wikipedia.org/wiki/Expectimax)

## Citation

1. [Heuristic functions](https://theresamigler.files.wordpress.com/2020/03/2048.pdf)
2. [Expectimax](https://osf.io/xfdsr)
