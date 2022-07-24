'''Test code'''
import random
from re import A
import game
from Grid import Grid
from utils import Maximizer, Minimizer
# Code chi choi 1 game.
# De choi duoc nhieu game, can phai kiem tra xem
# bang 
account = input("ACCOUNT_NAME : ")
quiz = input("QUIZ_NAME(1 , 2 , 3) : ")
client = game.Client(account , quiz)

while client.playing:
    data = client.get_state()

    if isinstance(data , game.Board):
        sz = len(data.board[0])
        Next_move = Maximizer(Grid(data.board) , 3)[0]
        print(f"Making the move {Next_move}")
        client.make_move(Next_move)
    elif isinstance(data , game.Game):
        print("Game ended")
    if isinstance(data , game.Result):
        print(f"Session ended with the score {data.point}")
        break