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
current_player_turn = True

print("hello world")

# Dice
def dice():
    roll = random.randint(1,6)
    # add to player location
    return roll

def move_player(player_location, outcome):
    player_location += outcome
    print(f"You move to tile {player_location}")
    return player_location

def player_turn():
    global player_1_location, player_2_location, turn
    if turn % 2 == 0:
        player_1_location = move_player(player_1_location, outcome)

    if turn % 2 == 1:
        player_2_location = move_player(player_2_location, outcome)


def end_game():
    ...

if __name__ == '__main__':
    print('Welcome to our bordgame')
    user_start = input('Would you like to play? y/n').strip().lower()
    if user_start == 'y':

        while True:
            if not current_player_turn:
                print("Next Player's turn!")
            current_player_turn = False
            roll_prompt = input("Press Enter to roll your dice!")
            input()
            outcome = dice()
            print(f"You rolled a {outcome}")
            player_turn()          
            if player_1_location == 3:
                question_tiles += 1
                choicequestions.questions(question_tiles)
            print(player_1_location)  
            print(player_2_location) 
            turn += 1            
            continue                     
    elif user_start == 'n':
        print('Goodbye')
        end_game()
    else:
        print('Invalid input')
        
    

