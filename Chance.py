
def chance(chance_number):
    #global turn
    
    while True:

    # mom hurts you, you lose scrap
        if chance_number == 1:
            player_choice = input('''You see a mother with a child,
            the child looks hurt.
            Do you help them? y/n ''')
            if player_choice == 'y':
                print('''The child was fine,
                they played you.
                The mom steals 20 scrap from you.''')
                # - 20 scrap
                reward = -20
                return reward
            elif player_choice == 'n':
                print('You walk away.')
                reward = 0
                return reward
            else:
                print('Invalid input')
        # mom is nice you gain scrap
        elif chance_number == 2:
            player_choice = input('''You see a mom with a child,
            they look hurt.
            Do you help them? y/n ''')
            if player_choice == 'y':
                print('''You help them,
                they are gratefull.
                They give you 15 scrap''')
                # + 15 scrap
                reward = 15
                return reward
            elif player_choice == 'n':
                print('You walk away.')
                reward = 0
                return reward
            else:
                print('Invalid input')
        # you see something shiny on the ground, pick it up? knife, you cut your finger
        elif chance_number == 3:
            player_choice = input('''You see something shiny on the ground.
            Do you pick it up? y/n ''')
            if player_choice == 'y':
                print('''You try to pick the item up,
                It's a gas mask!
                you can keep going for a while longer now.''')
                # extra turn

                reward = 0
                return reward
            elif player_choice == 'n':
                print('''You leave the item''')
                reward = 0
                return reward
            else:
                print('Invalid input')
        # your stomach grumbles, you see bugs. Eat? yummy extra roll
        elif chance_number == 4:
            player_choice = input('''You're hungry.
            Your stomach in grumbling.
            You see bugs running around.
            Do you eat them? y/n ''')
            if player_choice == 'y':
                print('''You choose to eat the bugs,
                you don\'t look at the while grabbing them.
                They taste fine,
                you\'re not hungry anymore.
                You roll again''')

                reward = 0
                return reward
                # extra turn
            elif player_choice == 'n':
                print('''You don\'t want to eat the bugs,
                you continue walking.
                but you\'re still hungry.''')
                reward = 0
                return reward
            else:
                print('Invalid input')
        # There's a hole in the ground, do you jump over? bad idea, you fall, skip turn
        elif chance_number == 5:
            player_choice = input('''You see a hole in the ground.
            Do you try to jump over it? y/n ''')
            if player_choice == 'y':
                print('''You try to jump over the hole,
                you barely make it, but lose your backpack in the process...
                you lose 20 scrap.''')
                reward = -20
                return reward
                # skip turn
            elif player_choice == 'n':
                print('''You walk around the hole.''')
                reward = 0
                return reward
            else:
                print('''Invalid input''')
        #something on the ground
        elif chance_number == 6:
            player_choice = input('''You see something on the ground,
            do you try to pick it up? y/n ''')
            if player_choice == 'y':
                print('''You pick it up,
                it\'s scraps!
                You gain 20 scraps.''')
                # + 20 scraps
                reward = 20
                return reward
            elif player_choice == 'n':
                print('''You leave it laying on the ground''')
                reward = 0
                return reward
            else:
                print('Invalid input')