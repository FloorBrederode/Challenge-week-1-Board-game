import random
# player gets a random item


def random_item():
    items = ['hat', 'shirt', 'pants', 'shoes', 'scrap']
    random_item = random.choice(items)

    if random_item == 'hat':
        return random_item
    elif random_item == 'shirt':
        return random_item
    elif random_item == 'pants':
        return random_item
    elif random_item == 'shoes':
        return random_item
    elif random_item == 'scrap':
        amount = random.randint(1,25)
        print(f'You get {amount} scrap')
        print(random_item)
        print(amount)
        return random_item, amount






print(random_item())