import random
import time


def displayIntro():
    print('You are in a land full of dragons. In front of you,')
    print('you see two caves. In one cave, the dragon is friendly')
    print('and will share his tresure with you. The other dragon')
    print ('is hungry and greedy, and eat you on sight.')
    print()

def chooseCave():
    cave = ''
    while cave != '1' and cave != '2':
        print('which cave will you go into? (1 or 2)')
        cave = input()
        #cave = input('which cave will you go into? (1 or 2)')

    return cave

def checkCave(chosenCave):
    print('You approach the cave...')
    time.sleep(2)
    print('It is dark and spooky...')
    time.sleep(2)
    print('A large dragon jumps out in front of you! He opens his jaws and...')
    print()
    time.sleep(2)

    friendlyCave = random.randint(1,2)

    if chosenCave == str(friendlyCave):
        print('Gives you his Tresure!')
    else:
        print('Gobbles you down in one bite!')

playagain = 'yes'
while playagain == 'yes' or playagain == 'y' or playagain == 'Y' or playagain == 'Yes' or playagain == 'YES':
    displayIntro()
    caveNumber = chooseCave()
    checkCave(caveNumber)
    print('Do you want to play again? (yes or no)')
    playagain = input()
