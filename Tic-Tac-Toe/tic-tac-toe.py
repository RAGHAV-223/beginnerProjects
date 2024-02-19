# Simple Tic-Tac-Toe game for two users or one user

import time
import random
from copy import copy

def print_board_state(bstate): # Function for printing Board
    print(f" { bstate[0] if bstate[0]!=0 else ' '} | { bstate[1] if bstate[1]!=0 else  ' '} | {bstate[2] if bstate[2]!=0 else ' '} ")
    print(f"---|---|---")
    print(f" {bstate[3] if bstate[3]!=0 else ' '} | {bstate[4] if bstate[4]!=0 else ' '} | {bstate[5] if bstate[5]!=0 else ' '} ")
    print(f"---|---|---")
    print(f" {bstate[6] if bstate[6]!=0 else ' '} | {bstate[7] if bstate[7]!=0 else ' '} | {bstate[8] if bstate[8]!=0 else ' ' } ")

def check_win(bstate): # Function for checking the winner
    for row in range(0,9,3):
        if (bstate[row] == bstate[row+1] == bstate[row+2]!=0):
            return bstate[row]
    for col in range(3):
        if (bstate[col] == bstate[col+3] == bstate[col+6] !=0):
            return bstate[col] 
    if (bstate[0]==bstate[4]==bstate[8] != 0) or (bstate[2] == bstate[4] == bstate[6] != 0):
        return bstate[4]
    
    if all(bstate):
        return -1
    return False
 
def two_players(): #Function for two user players
            # 0 1 2 3 4 5 6 7 8
    bstate = [0,0,0,0,0,0,0,0,0]
    turn = 1 # for X -> 1 , for Y -> 2
    while True:
        print_board_state(bstate)
        if (turn == 1):
            print("X's Turn")
            indx = int(input("Enter value: "))
            if bstate[indx-1]!=0:
                print("Invalid Move : Value aleady Filled")
                continue
            bstate[indx-1] = 'X'
            turn =2
        elif (turn == 2):
            print("O's Turn")
            indx = int(input("Enter value: "))
            if bstate[indx-1]!=0:
                print("Invalid Move : Value aleady Filled")
                continue
            bstate[indx -1] = 'O'
            turn = 1
        res= check_win(bstate)
        if res:
            print_board_state(bstate)
            if res == -1:
                print('It\s a Tie!')
            else:
                print(f"{res} won the match")
            break
            break

def one_player_easy():
    # 0 1 2 3 4 5 6 7 8
    bstate = [0,0,0,0,0,0,0,0,0]
    usr_symb = input("Enter your symbor (X or O): ").upper() # To get symbol for user
    comp_symb = ('X' if usr_symb=='O' else 'O') # assinging Symbol to computer
    turn= random.choice(['O','X'])
    print("First turn goes to ->", end="")
    time.sleep(0.8)
    print(turn)
    while True:
        print_board_state(bstate)
        if (turn == usr_symb):
            print("\nUser's Turn")
            indx = int(input("Enter value: "))
            if bstate[indx-1]!=0:
                print("Invalid Value")
                continue
            bstate[indx-1] = usr_symb
            turn = comp_symb
        else:
            print("\nComputer's Turn")
            valid_indx=[i if j==0 else None for i,j in enumerate(bstate)]
            indx=0
            while indx-1 not in valid_indx:
                indx = random.randint(1,9)
            bstate[indx -1] = comp_symb
            turn = usr_symb
            time.sleep(0.8)
        res = check_win(bstate)
        if res:
            print_board_state(bstate)
            if res == -1:
                print('It\s a Tie!')
            else:
                print(f"{res} won the match")
            break
            break

def one_player_hard():
           # 0 1 2 3 4 5 6 7 8
    bstate = [0,0,0,0,0,0,0,0,0]
    usr_symb = input("Enter your symbor (X or O): ").upper() # To get symbol for user
    comp_symb = ('X' if usr_symb=='O' else 'O') # assinging Symbol to computer
    turn= random.choice(['O','X'])
    print("First turn goes to ->", end="")
    time.sleep(0.8)
    print(turn)
    while True:
        print_board_state(bstate)
        if (turn == usr_symb):
            print("\nUser's Turn")
            indx = int(input("Enter value: "))
            if bstate[indx-1]!=0:
                print("Invalid Value")
                continue
            bstate[indx-1] = usr_symb
            turn = comp_symb
        else:
            print("\nComputer's Turn")
            valid_indx=list()
            for i,j in enumerate(bstate):
                if j==0:
                    valid_indx.append(i)
            indx = minmax_result(valid_indx,bstate,comp_symb)
            bstate[indx] = comp_symb
            turn = usr_symb
            time.sleep(0.8)
        res = check_win(bstate)
        if res:
            print_board_state(bstate)
            if res == -1:
                print('It\s a Tie!')
            else:
                print(f"{res} won the match")
            break

def empty_space(state):
    emp_lst=[]
    for i,j in enumerate(state):
           if j==0:
               emp_lst.append(i)
    return emp_lst

def minmax_result(valid_moves, state, symbl):
    bestscore = -1000
    bestmove = 0
    for move in empty_space(state):
        # make the move
        state[move]=symbl
        # check the score
        score = minmax(state,comp=symbl, ismax=False) 
        # undo the move
        state[move] = 0 
         
        if (score > bestscore):
            bestmove = move
            bestscore=score
    return bestmove

def minmax(state,comp, ismax):
    max_plr=comp
    other_plr= 'X' if comp=='O' else 'O'
    
    win=check_win(state)
    if win == other_plr:
        return -10
    elif win == max_plr:
        return 10
    elif win == -1:
        return 0
    
    # min-max algorithm
    if ismax:
        bestscore = -100000
        for move in empty_space(state):
            # make the move
            state[move]= max_plr
            # check the score
            score = minmax(state,comp=max_plr, ismax=False) 
            # undo the move
            state[move] = 0 

            if (score > bestscore):
                bestscore = score
        
        return bestscore
    else:
        bestscore = 100000
        for move in empty_space(state):
            # make the move
            state[move]=other_plr
            # check the score
            score = minmax(state,comp=max_plr, ismax=True) 
        
            # undo the move
            state[move] = 0           
            if (score < bestscore):
                bestscore = score
        
        return bestscore   



if __name__=="__main__":
    print("\n****** welcome to Tic Tac Toe ******\nPlease enter the value of box in order to fill  it on your turn")
    print(" 1 | 2 | 3 ")
    print("---|---|---")
    print(" 4 | 5 | 6 ")
    print("---|---|---")
    print(" 7 | 8 | 9 \n\n\t<----> The game beginns <---->")
    print("Main Menu")
    choice = input("For Two Players -> 1 \nFor One Player Easy -> 2 \nFor One Player Normal -> 3\t:")
    if choice == '1':
        two_players()
    elif choice == '2':
        one_player_easy()
    elif choice == '3':
        one_player_hard()
    else:
        print("Invalid Choice")
    

