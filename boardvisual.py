
def visualize_board(player_1_location, player_2_location):
    if int(player_1_location) >= 100:
        print("Player 1 has won the game!")
        return
    if int(player_2_location) >= 100:
        print("Player 2 has won the game!")
        return

    board = '''
    1  | 2  | 3  | 4  | 5  | 6  | 7  | 8  | 9  | 10 |
    20 | 19 | 18 | 17 | 16 | 15 | 14 | 13 | 12 | 11 |
    21 | 22 | 23 | 24 | 25 | 26 | 27 | 28 | 29 | 30 |
    40 | 39 | 38 | 37 | 36 | 35 | 34 | 33 | 32 | 31 |
    41 | 42 | 43 | 44 | 45 | 46 | 47 | 48 | 49 | 50 |
    60 | 59 | 58 | 57 | 56 | 55 | 54 | 53 | 52 | 51 |
    61 | 62 | 63 | 64 | 65 | 66 | 67 | 68 | 69 | 70 |
    80 | 79 | 78 | 77 | 76 | 75 | 74 | 73 | 72 | 71 |
    81 | 82 | 83 | 84 | 85 | 86 | 87 | 88 | 89 | 90 |
    100| 99 | 98 | 97 | 96 | 95 | 94 | 93 | 92 | 91 |
    '''
    
    
    player_board = board.replace(f' {player_1_location} ', f' \033[1;31mP1\033[0m ').replace(f' {player_2_location} ', f' \033[1;32mP2\033[0m ')
    print(player_board)
    
    print("\n")