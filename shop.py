# what to buy in shop
# hat
# shirt
# pants
# shoes
# extra roll
# idk something else

def shop(player_scrap):
    scrap = player_scrap
    print('Welcome to the shop!')
    print(f'You have {scrap} scrap')
    shop_answer = input('Would you like to buy something? y/n ').lower().strip()
    while True:
        if shop_answer == 'y':
            print('''We have,
            - [A] Hats...(Scrap)
            - [B] Shirts...(Scrap)
            - [C] Pants...(Scrap)
            - [D] Shoes...(Scrap)
            - [E] An extra Roll...(Scrap)''')
            player_buying = input('Is there something you want? ')
            if player_buying == 'a':
                break
            elif player_buying == 'b':
                break
            elif player_buying == 'c':
                break
            elif player_buying == 'd':
                break
            elif player_buying == 'e':
                break
            else:
                print('We dont sell that.')
        elif shop_answer == 'n':
            print('Goodbye!')
            break
        else:
            print('Invalid input')


player_1_scrap = 15
shop(player_1_scrap)
