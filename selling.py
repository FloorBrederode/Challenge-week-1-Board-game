

def selling(player_scrap, player_inventory):
    scrap = player_scrap
    sellable_items = player_inventory

    while True:
        player_answer = input(f'''
        Welcome to the pawn shop.
        Would you like to sell something? y/n
        Here is what you have on you:
        {sellable_items}
        ''').lower().strip()
    
        if player_answer == 'y':
            item_to_sell = input('''
        Which item would you like to sell?
        Please write out which item.
        If you wish to leave enter [e].
            ''').lower().strip()
        # Hats
            if item_to_sell == 'hat':
                if 'hat' in sellable_items:
                    print('''
        You sell your hat.
        it sells for 5 scrap.
        ''')
                    sellable_items.remove('hat')
                    scrap += 5
                    return sellable_items, scrap
                else:
                    print('''
            You don\'t have a hat.''')
        # Shirts
            elif item_to_sell == 'shirt':
                if 'shirt' in sellable_items:
                    print('''
        You sell your shirt.
        it sells for 10 scrap.
        ''')
                    sellable_items.remove('shirt')
                    scrap += 10
                    return sellable_items, scrap
                else:
                    print('''
            You don\'t have a shirt.''')
        # Pants
            elif item_to_sell == 'pants':
                if 'pants' in sellable_items:
                    print('''
        You sell your pants.
        it sells for 15 scrap.
        ''')
                    sellable_items.remove('pants')
                    scrap += 15
                    return sellable_items, scrap
                else:
                    print('''
            You don\'t have pants.''')
        # Shoes
            elif item_to_sell == 'shoes':
                if 'shoes' in sellable_items:
                    print('''
        You sell your shoes.
        it sells for 20 scrap.
        ''')
                    sellable_items.remove('shoes')
                    scrap += 20
                    return sellable_items, scrap
                else:
                    print('''
            You don\'t have shoes.''')
            elif item_to_sell == 'e':
                print('Goodbye.')
                return 'nothing'
            else:
                print('Invalid input 1')
        elif player_answer == 'n':
            print('Goodbye.')
            return 'nothing'
        else:
            print('Invalid input 2')

