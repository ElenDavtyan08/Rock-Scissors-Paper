from random import choice

GAME_DICT = {
    'r' : 'Rock',
    'p' : 'Paper',
    's' : "Scissors"
}
INFO = {
    'wins' : 0,
    'losses' : 0,
    'ties' : 0
}

def computer():
    move = choice(list(GAME_DICT.keys()))
    return move

def print_moves(player_move, comp_move):
    print(f'{GAME_DICT[player_move]} VS {GAME_DICT[comp_move]}')

def determine_winner(player_move, comp_move):

    if player_move == comp_move:
        print('It is a tie')
        INFO['ties'] += 1
        print(INFO)
        
    elif (player_move == 'r' and comp_move == 's') or \
        (player_move == 'p' and comp_move == 'r') or \
        (player_move == 's' and comp_move == 'p'):
        print('You WIN!')
        INFO['wins'] += 1 
        print(INFO)

    else:
        print('You lose :(')
        INFO['losses'] += 1
        print(INFO)

