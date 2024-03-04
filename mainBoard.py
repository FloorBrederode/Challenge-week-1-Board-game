import random

player_1 = 0
player_2 = 0

# Dice
def dice():
    roll = random.randint(1,6)
    return roll


if __name__ == '__main__':
    print(dice())