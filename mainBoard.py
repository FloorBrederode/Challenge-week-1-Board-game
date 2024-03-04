import random


# player location
player_1 = 0
player_2 = 0
# starting scrap
# make lists for both players so they can collect clothes
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
