#date 04-16-24
#my version of tic tac toe game

import os 
import time


def name_players():
    
    global  names
    player1 = input("Whats the name of Player 1: ")
    player2 = input("Whats the name of Player 2: ")
    names = player1.upper(),'VS',player2.upper()
    os.system('clear')
    

def board_game1 ():

    a = [' ',' ',' ']
    b = [' ',' ',' ']
    c = [' ',' ',' ']
    print("----------------")
    print('BEST GAME EVER')
    print("----------------")
    print(a)
    print(b)
    print(c)
    print("----------------")
    print(names)
    print("----------------")
    time.sleep(3)
    os.system('clear')

    print('These are the numbers for each position in the board')

    a = ['1','2','3']
    b = ['4','5','6']
    c = ['7','8','9']
    print("----------------")
    print('BEST GAME EVER')
    print("----------------")
    print('\n',a,'\n',b,'\n',c)
    print("----------------")
    print(names)
    print("----------------")
    time.sleep(10)
    os.system('clear')

game_list1 = [' ',' ',' ']
game_list2 = [' ',' ',' ']
game_list3 = [' ',' ',' ']

def real_board_game(game_list1,game_list2,game_list3):
    print("Here's the current board")
    print(names)
    print('\n',game_list1,'\n',game_list2,'\n',game_list3)


#naming the players
name_players()

#board game showing names
board_game1()

#board game geting values
real_board_game(game_list1,game_list2,game_list3)    



