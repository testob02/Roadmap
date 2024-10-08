import random

box_states = [i+1 for i in range(9)]


def ask_game_mode():
    game_mode = None
    while game_mode != 1 or game_mode != 2:
        game_mode = int(input("Which game mode:\nEnter 1 for vs CPU\nEnter 2 for vs player\n"))
        if game_mode == 1 or game_mode == 2:
            break
    return game_mode

def user_input():
    print('\n\n')
    user_inp = int(input("Enter your move:\t"))
    while check_if_box_filled(user_inp-1,box_states):
        user_inp = int(input("Enter your move:\t"))
    box_states[user_inp-1] = 'O'
    print('\n\n')

def multi_input(player_num):
    print('\n\n')
    user_inp = int(input(f"Player {player_num} Enter your move:\t"))
    while check_if_box_filled(user_inp-1,box_states):
        user_inp = int(input(f"Player {player_num} Enter your move:\t"))
    if player_num == 1:
        box_states[user_inp-1] = 'X'
    elif player_num == 2:
        box_states[user_inp-1] = 'O'
    print('\n\n')

def get_computer_input():
    print('Computer is making its move\n\n')
    comp_inp = random.choice(all_empty_boxes(box_states))
    box_states[comp_inp] = 'X'
    
def check_if_box_filled(box,box_states):
    return box_states[box] == 'X' or box_states[box] == 'O'

def all_empty_boxes(box_states):
    empty_boxes = []
    for box in range(9):
        if not check_if_box_filled(box,box_states):
            empty_boxes.append(box)

    return empty_boxes

def check_game_state(box_states):
    if box_states[0] == box_states[1] == box_states[2]:
        return box_states[0]
    
    if box_states[3] == box_states[4] == box_states[5]:
        return box_states[3]
    
    if box_states[6] == box_states[7] == box_states[8]:
        return box_states[6]
    
    if box_states[0] == box_states[4] == box_states[8]:
        return box_states[0]
    
    if box_states[2] == box_states[4] == box_states[6]:
        return box_states[2]
    
    if box_states[0] == box_states[3] == box_states[6]:
        return box_states[0]
    
    if box_states[1] == box_states[4] == box_states[7]:
        return box_states[1]
    
    if box_states[2] == box_states[5] == box_states[8]:
        return box_states[2]
    
    empty_box = False
    for box in range(9):
        if check_if_box_filled(box,box_states) is False:
            empty_box = True
            break

    if empty_box == False:
        return "Tie"
    
    return "game"
    
def get_winner(box_states):
    state = check_game_state(box_states)
    if state == "game":
        return
    elif state == 'X':
        return "Computer wins"
    elif state == 'O':
        return "User wins"
    elif state == 'Tie':
        return "Tie"
    
def get_multi_winner(box_states):
    state = check_game_state(box_states)
    if state == "game":
        return
    elif state == 'X':
        return "Player 1 wins"
    elif state == 'O':
        return "Player 2 wins"
    elif state == 'Tie':
        return "Tie"

def print_gui(box_states):
    print('*************************')
    print('*\t*\t*\t*')
    print(f'*   {box_states[0]}\t*   {box_states[1]}\t*   {box_states[2]}\t*')
    print('*\t*\t*\t*')
    print('*************************')
    print('*\t*\t*\t*')
    print(f'*   {box_states[3]}\t*   {box_states[4]}\t*   {box_states[5]}\t*')
    print('*\t*\t*\t*')
    print('*************************')
    print('*\t*\t*\t*')
    print(f'*   {box_states[6]}\t*   {box_states[7]}\t*   {box_states[8]}\t*')
    print('*\t*\t*\t*')
    print('*************************')

def single_game_loop():
    while check_game_state(box_states) == 'game':
        get_computer_input()
        print_gui(box_states)
        winner = get_winner(box_states)
        if winner:
            print('\n')
            print(winner.upper())
            break
        user_input()
        print_gui(box_states)
        winner = get_winner(box_states)
        if winner:
            print('\n')
            print(winner.upper())
            break

def multi_game_loop():
    print_gui(box_states)
    while check_game_state(box_states) == 'game':
        multi_input(1)
        print_gui(box_states)
        winner = get_multi_winner(box_states)
        if winner:
            print('\n')
            print(winner.upper())
            break
        multi_input(2)
        print_gui(box_states)
        winner = get_multi_winner(box_states)
        if winner:
            print('\n')
            print(winner.upper())
            break

mode = ask_game_mode()
if mode == 1:
    single_game_loop()
elif mode == 2:
    multi_game_loop()

    

