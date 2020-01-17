# -*- coding: utf-8 -*-
"""
Created on Sat Jun 29 23:20:04 2019

@author: Srinjoy
"""

board=[" " for i in range(9)]

def print_board():
    row1="\t{}|{}|{}".format(board[0],board[1],board[2])
    row2="\t{}|{}|{}".format(board[3],board[4],board[5])
    row3="\t{}|{}|{}".format(board[6],board[7],board[8])
    print()
    print(row1)
    print(row2)
    print(row3)
    print()

def player_mv(icon):
    while True:
        choice=int(input("Where do you wanna place? :").strip())
        if(board[choice-1]==" "):
            board[choice-1]=icon
            break
        else:
            print()
            print("Nope! That space is taken !")

def is_draw():
    if " " not in board:
        return True
    else:
        return False

def is_win(icon):
    if(board[0]==icon and board[1]==icon and board[2]==icon or \
       board[3]==icon and board[4]==icon and board[5]==icon or \
       board[6]==icon and board[7]==icon and board[8]==icon or \
       board[0]==icon and board[3]==icon and board[6]==icon or \
       board[1]==icon and board[4]==icon and board[7]==icon or \
       board[2]==icon and board[5]==icon and board[8]==icon or \
       board[0]==icon and board[4]==icon and board[8]==icon or \
       board[2]==icon and board[4]==icon and board[6]==icon):
        return True
    else:
        return False

while True:
    print_board()
    player_mv('x')
    print_board()
    if(is_win('x')):
        print('X wins !')
        break
    elif(is_draw()):
        print("It's a draw !")
        break
    player_mv('o')
    if(is_win('o')):
        print_board()
        print('O wins !')
        break
    elif(is_draw()):
        print("It's a draw !")
        break
    

