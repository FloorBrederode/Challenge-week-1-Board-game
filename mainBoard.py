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

print("hello world")

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
        end_game()
    else:
        print('Invalid input')
        


    roll_prompt = input("Player type Roll to roll your dice!")
    if roll_prompt == "Roll":
        if turn % 2 == 0:
            player_1_location += dice()
            print(f"Survivor 1 moves {dice()} steps...")
            break
        if turn % 2 == 1:
            player_2_location += dice()
            print(f"Survivor 2 moves {dice()} steps...")
        
    

