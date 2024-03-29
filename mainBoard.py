import random

import Chance
import choicequestions
import shop
import selling
import randomitem
import boardvisual

import os



# Types of tiles
multiple_choice_tiles = [5, 21, 36, 48, 66, 76]
shop_tiles = [10, 30, 50, 70, 90]
sell_tiles = [20, 40, 60, 80]
random_item = [12, 43, 57, 77, 92]
chance_tiles = [8, 24, 41, 64, 85, 94]


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
    global turn, question_tiles, chance_number

    # player 1
    global player_1_location, player_1_scrap, player_1_list
    if turn % 2 == 0:
        print('Player 1')
        print(f"You rolled a {outcome}")
        player_1_location = move_player(player_1_location, outcome)

        # multiple choice questions 
        if player_1_location in multiple_choice_tiles:
            question_tiles += 1
            reward = choicequestions.questions(question_tiles)
            player_1_scrap += reward
            print(f'Player 1 now has {player_1_scrap} scrap.')

        # shop
        elif player_1_location in shop_tiles:

            while True:
                store_answer = input(f'''You land on a store Tile.
            You have {player_1_scrap} scrap.
            Do you enter the store? y/n ''').lower().strip()

                if store_answer == 'y':
                    items_bought = shop.shop(player_1_scrap)
                    print(items_bought)
                    if len(items_bought) == 2:
                        player_1_scrap = int(items_bought[0])
                        print(player_1_scrap)
                        player_1_list.append(items_bought[1])
                        print(player_1_list)
                    break
                elif store_answer == 'n':
                    break
                else:
                    print('Invalid input')

        # Pawn Shop
        elif player_1_location in sell_tiles:

            while True:
                pawn_shop_answer = input('''
                You land on a pawn shop tile.
                Do you enter? y/n ''').lower().strip()

                if pawn_shop_answer == 'y':
                    new_items = selling.selling(player_1_scrap, player_1_list)
                    if len(new_items) == 2:
                        player_1_list = new_items[0]
                        player_1_scrap = new_items [1]
                        break
                elif pawn_shop_answer == 'n':
                    break
                else:
                    print('Invalid input')


        # Chance encounters
        elif player_1_location in chance_tiles: 
            player_1_scrap += Chance.chance(chance_number)
            print(f"You now have {player_1_scrap} scrap")
            chance_number += 1

        # snakes
        elif player_1_location == 45:
            print('''
            OH NO!
            You landed on a snake tile.
            You go back to tile 27.
            ''')
            player_1_location = 27
        elif player_1_location == 68:
            print('''
            OH NO!
            You landed on a snake tile.
            You go back to tile 54.
            ''')
            player_1_location = 54
        elif player_1_location == 82:
            print('''
            OH NO!
            You landed on a snake tile.
            You go back to tile 61.
            ''')
            player_1_location = 61
        elif player_1_location == 96:
            print('''
            OH NO!
            You landed on a snake tile.
            You go back to tile 75.
            ''')
            player_1_location = 75

        #ladders
        elif player_1_location == 13:
            print('''
            NICE!
            You landed on a ladder!
            You go to tile 32.
            ''')
            player_1_location = 32
        elif player_1_location == 17:
            print('''
            NICE!
            You landed on a ladder!
            You go to tile 39.
            ''')
            player_1_location = 39
        elif player_1_location == 46:
            print('''
            NICE!
            You landed on a ladder!
            You go to tile 56.
            ''')
            player_1_location = 56
        elif player_1_location == 67:
            print('''
            NICE!
            You landed on a ladder!
            You go to tile 88.
            ''')
            player_1_location = 88
        

        # Random item
        elif player_1_location in random_item:
            item_given = randomitem.random_item()
            item_given_list = [item_given]
            print(f'''
            You land on a random item tile.
            You get: {item_given}''')
            print(item_given)
            player_1_list.append(item_given)
            print(f'Your inventory: {player_1_list}')

    # player 2
    global player_2_list, player_2_location, player_2_scrap

    if turn % 2 == 1:
        print('Player 2')
        print(f"You rolled a {outcome}")
        player_2_location = move_player(player_2_location, outcome)

        # multiple choice questions
        if player_2_location in multiple_choice_tiles:
            question_tiles += 1
            reward = choicequestions.questions(question_tiles)
            player_2_scrap += reward
            print(f'Player 2 now has {player_2_scrap} scrap.')

        elif player_2_location in shop_tiles:

            # shop
            while True:
                store_answer = input(f'''You land on a store Tile.
                You have {player_2_scrap} scrap.
                Do you enter the store? y/n ''').lower().strip()

                if store_answer == 'y':
                    items_bought = shop.shop(player_2_scrap)
                    print(items_bought)
                    if len(items_bought) == 2:
                        player_2_scrap = int(items_bought[0])
                        print(player_2_scrap)
                        player_2_list.append(items_bought[1])
                        print(player_2_list)
                    break
                elif store_answer == 'n':
                    break
                else:
                    print('Invalid input')

        # Pawn Shop
        elif player_2_location in sell_tiles:

            while True:
                pawn_shop_answer = input('''
                You land on a pawn shop tile.
                Do you enter? y/n ''').lower().strip()

                if pawn_shop_answer == 'y':
                    new_items = selling.selling(player_2_scrap, player_2_list)
                    if len(new_items) == 2:
                        player_2_list = new_items[0]
                        player_2_scrap = new_items [1]
                        break
                elif pawn_shop_answer == 'n':
                    break
                else:
                    print('Invalid input')

        # Chance encounters
        elif player_2_location in chance_tiles: 
            player_2_scrap += Chance.chance(chance_number)
            print(f"You now have {player_2_scrap} scrap")
            chance_number += 1

        # snakes
        elif player_2_location == 45:
            print('''
            OH NO!
            You landed on a snake tile.
            You go back to tile 27.
            ''')
            player_2_location = 27
        elif player_2_location == 68:
            print('''
            OH NO!
            You landed on a snake tile.
            You go back to tile 54.
            ''')
            player_2_location = 54
        elif player_2_location == 82:
            print('''
            OH NO!
            You landed on a snake tile.
            You go back to tile 61.
            ''')
            player_2_location = 61
        elif player_2_location == 96:
            print('''
            OH NO!
            You landed on a snake tile.
            You go back to tile 75.
            ''')
            player_2_location = 75

        #ladders
        elif player_2_location == 13:
            print('''
            NICE!
            You landed on a ladder!
            You go to tile 32.
            ''')
            player_2_location = 32
        elif player_2_location == 17:
            print('''
            NICE!
            You landed on a ladder!
            You go to tile 39.
            ''')
            player_2_location = 39
        elif player_2_location == 46:
            print('''
            NICE!
            You landed on a ladder!
            You go to tile 56.
            ''')
            player_2_location = 56
        elif player_2_location == 67:
            print('''
            NICE!
            You landed on a ladder!
            You go to tile 88.
            ''')
            player_2_location = 88

        # Random item
        elif player_2_location in random_item:
            item_given = randomitem.random_item()
            item_given_list = [item_given]
            print(f'''
            You land on a random item tile.
            You get: {item_given}''')
            print(item_given)
            player_2_list.append(item_given)
            print(f'Your inventory: {player_2_list}')
        


if __name__ == '__main__':
    print('Welcome to our bordgame')
    print('''The theme of this boardgame is a nuclear distopian.
    The main objective is to get to tile 100 first.
    There is a side objective, by collecting a complete outfit you get an extra reward.''')

    while True:    
        user_start = input('Would you like to play? y/n ').strip().lower()
        if user_start == 'y':

            # player location
            player_1_location = 1
            player_2_location = 1
            # starting scrap
            player_1_scrap = 25
            player_2_scrap = 25
            # make lists for both players so they can collect clothes
            player_1_list = []
            player_2_list = []
            # which player is playing by doing math
            turn = 0
            current_player_turn = True

            number_question = 0
            chance_number = 1
            question_tiles = 0

            while player_1_location < 100 and player_2_location < 100:
                if not current_player_turn:
                    print("Next Player's turn!")
                current_player_turn = False
                roll_prompt = input("Press Enter to roll your dice!")
                outcome = dice()
                os.system('cls')
                player_turn()

                # visual of the board
                player_1_tile = f'{player_1_location}'
                player_2_tile = f'{player_2_location}'
                boardvisual.visualize_board(player_1_tile, player_2_tile)

                #scrap can't fall below 0
                if player_1_scrap < 0:
                    player_1_scrap = 0 
                if player_2_scrap < 0:
                    player_2_scrap = 0
                
                print(f'Player 1 location: Tile {player_1_location}')
                print(f'Player 2 location: Tile {player_2_location}')
                turn += 1            
                continue                     
        elif user_start == 'n':
            print('Goodbye')
            break
        else:
            print('Invalid input')
        
    

