import random

wins = 0

for i in range(100_000):
    doors = [True, False, False]

    random.shuffle(doors)

    my_door = random.choice([0,1,2])

    while True:
        show_door = random.choice([0,1,2])
        if show_door == my_door:
            continue
        if not doors[show_door]:
            break

    for other_door in range(3):
        if other_door == show_door:
            continue
        if other_door == my_door:
            continue
        break

    #chosen_door = my_door
    chosen_door = other_door

    if doors[chosen_door]:
        wins += 1

print(wins)