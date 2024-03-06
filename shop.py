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
            - [A] Hats...(10 Scrap)
            - [B] Shirts...(15 Scrap)
            - [C] Pants...(20 Scrap)
            - [D] Shoes...(30 Scrap)
            - [E] An extra Roll...(50 Scrap)
            [L] Leave''')

            player_buying = input('Is there something you want? ')

            if player_buying == 'a':
                if scrap < 10:
                    print('You don\'t have enough scrap to buy this')
                    input()
                elif scrap > 10:
                    print('Here\'s your new hat.')
                    scrap -= 10
                    print(scrap)
                    input()
            elif player_buying == 'b':
                if scrap < 15:
                    print('You don\'t have enough scrap to buy this')
                    input()
                elif scrap > 15:
                    print('Here\'s your new hat.')
                    scrap -= 15
                    print(scrap)
                    input()
                break
            elif player_buying == 'c':
                if scrap < 20:
                    print('You don\'t have enough scrap to buy this')
                    input()
                elif scrap > 20:
                    print('Here\'s your new hat.')
                    scrap -= 20
                    print(scrap)
                    input()
                break
            elif player_buying == 'd':
                if scrap < 30:
                    print('You don\'t have enough scrap to buy this')
                    input()
                elif scrap > 30:
                    print('Here\'s your new hat.')
                    scrap -= 30
                    print(scrap)
                    input()
                break
            elif player_buying == 'e':
                if scrap < 50:
                    print('You don\'t have enough scrap to buy this')
                    input()
                elif scrap > 50:
                    print('Here\'s your new hat.')
                    scrap -= 50
                    print(scrap)
                    input()
                break
            elif player_buying == 'l':
                print('Goodbye')
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
