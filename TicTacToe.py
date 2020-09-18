#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from IPython.display import clear_output

def display_board(board):
    clear_output()
    
    print(board[7]+' | '+board[8]+' | '+board[9])
    print('--|---|--')
    print(board[4]+' | '+board[5]+' | '+board[6])
    print('--|---|--')
    print(board[1]+' | '+board[2]+' | '+board[3])
    
    

def player_input():
    marker = ''
    while marker != 'X' and marker != 'O':
        marker = input("Player 1, Choose X or O: ")
        
    player1 = marker
    
    if player1 == 'X':
        player2 = 'O'
    else:
        player2 = 'X'
    
    return(player1,player2)



def place_marker(board, marker, position):
    board[position] = marker
    
    
    
def win_check(board, marker):
    return(board[1]==board[2]==board[3]==marker or
    board[4]==board[5]==board[6]==marker or
    board[7]==board[8]==board[9]==marker or
    board[1]==board[4]==board[7]==marker or
    board[2]==board[5]==board[8]==marker or
    board[3]==board[6]==board[9]==marker or
    board[1]==board[5]==board[9]==marker or
    board[3]==board[5]==board[7]==marker)



import random

def choose_first():
    chosen_player = random.randint(1,2)
    return(str(chosen_player))



def space_check(board, position):
    return(board[position] == ' ')



def full_board_check(board):
    full = True
    
    for pos in range(len(board)):
        if space_check(board,pos):
            full = False
    return(full)



def player_choice(board):
    
    choice = 0
    
    while choice<1 or choice>9 or not space_check(board,choice):
        choice = int(input("Choose you next position (1-9): "))
        
    return(choice)
        
        
        
def replay():
    play_again = input("Do you want to play again? Enter Yes or No: ")
    return(play_again == "Yes")




print('Welcome to Tic Tac Toe!')
    
while True:
    
    board = ['#',' ',' ',' ',' ',' ',' ',' ',' ',' ']
    
    player1_marker, player2_marker = player_input()
    player_turn = choose_first()
    print('Player'+player_turn+' goes first')
    
    ready = "No"
    while ready != "Yes":
        ready = input("Are you ready to play? Enter Yes or No: ")
        
    if ready == "Yes": game_on = True
        
    while game_on == True:
        
         if player_turn == '1':
            display_board(board)
            next_pos = player_choice(board)
            place_marker(board,player1_marker,next_pos)
            if win_check(board,player1_marker):
                display_board(board)
                print("Congratulations, Player 1 has won the game!")
                game_on = False
            elif full_board_check(board):
                display_board(board)
                print("It's a tie!")
                game_on = False
            else:
                player_turn = '2'       
         else:
            display_board(board)
            next_pos = player_choice(board)
            place_marker(board,player2_marker,next_pos)
            if win_check(board,player2_marker):
                display_board(board)
                print("Congratulations, Player 2 has won the game!")
                game_on = False
            elif full_board_check(board):
                display_board(board)
                print("It's a tie!")
                game_on = False
            else:
                player_turn = '1'
    
    if  not replay():
        print("Thank You for playing!")
        break

