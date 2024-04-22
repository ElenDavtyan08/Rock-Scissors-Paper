from helpers import print_moves, computer, determine_winner, GAME_DICT

def play_game():
    move = input('Enter your move: ').lower()
    if move == "q":
        return False
    elif move not in GAME_DICT:
        print("Invalid input! Please enter 'r', 'p' or 's', 'q' for quit")
    else:
        comp_move = computer()
        print_moves(move, comp_move)
        determine_winner(move, comp_move)
    return True
