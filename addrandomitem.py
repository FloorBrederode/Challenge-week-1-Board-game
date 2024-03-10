import randomitem

player_1_location = 10
player_1_list = []

random_item = [10]
 
# Random item
def get_item():
    if player_1_location in random_item:
        item_given = randomitem.random_item()
        item_given_list = [item_given]
        print(f'''
        You land on a random item tile.
        You get: {item_given}''')
        print(item_given)
        player_1_list.append(item_given)
        print(player_1_list)
