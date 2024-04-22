from game_programme import play_game

if __name__ == '__main__':
    print("Let's play (r)ock, (s)issors, (p)aper")
    
    while True:
        game_result = play_game()
        if not game_result:
            break
    print('You quit the game. Thanks!')
