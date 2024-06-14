import random

Player = int(input('=================== \n'
                   'Rock Paper Scissors \n'
                   '=================== \n'
                   '1) ✊ \n'
                   '2) ✋ \n'
                   '3) ✌️ \n'
                   'Pick a Number: '))

random_number = random.randint(1, 3)

if Player == 1:
    print()
    print('You chose: ✊')
elif Player == 2:
    print()
    print('You chose: ✋')
elif Player == 3:
    print()
    print('You chose: ✌️')
else:
    print()
    print('You chose: ⚠️')

if random_number == 1:
    print('CPU chose: ✊')
elif random_number == 2:
    print('CPU chose: ✋')
elif random_number == 3:
    print('CPU chose: ✌️')
else:
    print('CPU chose: ⚠️')

if Player == 1:
    if random_number == 1:
        print("It's a Tie!")
    elif random_number == 2:
        print("The CPU won!")
    elif random_number == 3:
        print("The player won!")
    else:
        print("INVALID ROUND!")

if Player == 2:
    if random_number == 2:
        print("It's a Tie!")
    elif random_number == 3:
        print("The CPU won!")
    elif random_number == 1:
        print("The player won!")
    else:
        print("INVALID ROUND!")

if Player == 3:
    if random_number == 3:
        print("It's a Tie!")
    elif random_number == 1:
        print("The CPU won!")
    elif random_number == 2:
        print("The player won!")
    else:
        print("INVALID ROUND!")

if Player > 3 or Player <= 0:
    print("INVALID ROUND!")

if random_number > 3 or random_number <= 0:
    print("INVALID ROUND!")