import random


# player location
player_1_location = 0
player_2_location = 0
# starting scrap
player_1_scrap = 0
player_2_scrap = 0
# make lists for both players so they can collect clothes
player_1_list = []
player_2_list = []
# which player is playing by doing math
turn = 0

# Dice
def dice():
    roll = random.randint(1,6)
    # add to player location
    return roll


def end_game():
    ...


if __name__ == '__main__':
    print('Welcome to our bordgame')
    user_start = input('Would you like to play? y/n').strip().lower()
    if user_start == 'y':
        ...
    elif user_start == 'n':
        print('Goodbye')
        endgame()
    else:
        print('Invalid input')
