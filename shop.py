# what to buy in shop
# hat
# shirt
# pants
# shoes
# extra roll
# idk something else

def shop(player_scrap):
    scrap = player_scrap

    while True:
            print('''We have,
            - [A] Hats...(10 Scrap)
            - [B] Shirts...(15 Scrap)
            - [C] Pants...(20 Scrap)
            - [D] Shoes...(30 Scrap)
            [L] Leave''')

            player_buying = input('Is there something you want? ')

            if player_buying == 'a':
                if scrap < 10:
                    print('You don\'t have enough scrap to buy this')
                    input()
                else:
                    print('Here\'s your new hat.')
                    scrap -= 10
                    input()
                    return (scrap, 'hat')
                    # it needs to return the amount of scrap now had and an item
            elif player_buying == 'b':
                if scrap < 15:
                    print('You don\'t have enough scrap to buy this')
                    input()
                else:
                    print('Here\'s your new shirt.')
                    scrap -= 15
                    input()
                    return (scrap, 'shirt')
                break
            elif player_buying == 'c':
                if scrap < 20:
                    print('You don\'t have enough scrap to buy this')
                    input()
                else:
                    print('Here\'s your new pants.')
                    scrap -= 20
                    input()
                    return (scrap, 'pants')
                break
            elif player_buying == 'd':
                if scrap < 30:
                    print('You don\'t have enough scrap to buy this')
                    input()
                else:
                    print('Here are your new shoes.')
                    scrap -= 30
                    input()
                    return (scrap, 'shoes')
                break
            elif player_buying == 'l':
                print('Goodbye')
                break
            else:
                print('We dont sell that.')
            print('Goodbye!')
            break


player_1_scrap = 15
