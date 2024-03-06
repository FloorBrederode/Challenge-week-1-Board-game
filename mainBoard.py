import random
import choicequestions

number_question = 0

question_tiles = 0
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

def move_player(player_location, outcome):
    player_location += outcome
    print(f"You move {outcome} steps...")
    return player_location

def end_game():
    ...

if __name__ == '__main__':
    print('Welcome to our bordgame')
    user_start = input('Would you like to play? y/n').strip().lower()
    if user_start == 'y':

        while True:
            roll_prompt = input("Press Enter to roll your dice!")
            input()
            outcome = dice()
            print(f"You rolled a {outcome}")
            if turn % 2 == 0:
                player_1_location = move_player(player_1_location, outcome)
                if player_1_location == 3:
                    question_tiles += 1
                    choicequestions.questions(question_tiles)              
                continue
            if turn % 2 == 1:
                continue 
                
    elif user_start == 'n':
        print('Goodbye')
        end_game()
    else:
        print('Invalid input')
        
    

