from datetime import datetime
from random import randint

name = 'Tom'

print('Hello', name)

print('Python math solution:', 1+2*3)
print('Date and time is', datetime.now())

def roll_dice():
    print('You rolled a', randint(1, 6))

roll_dice()

def roll_d():    
    max = input('How many sides?:')
    print('That\'s a D', max)
    roll = randint(1, int(max))
    print('You rolled a', roll)

roll_d()