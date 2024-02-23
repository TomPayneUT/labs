import datetime

#Variable is a named piece of information
user = 'Tom' #input('What is your name?: ')
age = 22
isCool = True

#Function is a named set of instructions
print('Hello', user)

def add_nums(x, y):
    #instructions go here
    result = x+y  #+ - * /
    print(result)

print('This is not inside the function')

add_nums(3, 5)
add_nums(32423, 23454)

print((1+2)*3)

today  = datetime.date(1776, 7, 4)
print(today.weekday())

# Flow control
if age >= 18:
    print('You can vote')
elif age >= 16:
    print('You can drive')
else:
    print('You are too young')

#Loop - repeats code
    
balance = 100000

#for day in range(30):
while 0 < balance < 1000000:
    balance *= 2
    print(balance)

