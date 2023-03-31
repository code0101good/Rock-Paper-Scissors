import random

rps = ['Rock', 'Paper', 'Scissors']



def result(entryRPS):
    if entryRPS == 1:   #here 1 is rock
        print(random.choices(rps))
    elif entryRPS == 2: #here 1 is paper
        print(random.choices(rps))
    elif entryRPS == 3: #here 1 is scissor
        print(random.choices(rps))
    else:
        print('Error!....')

    # entryRPS = input('Enter the number: ')

print(result(2))