print('Hello! My name is Aid.')
print('I was created in 2020.')
print('Please, remind me your name.')

name = input()

print('What a great name you have, ' + name + '!')
print('Let me guess your age.')
print('Enter remainders of dividing your age by 3, 5 and 7.')

r = [int(input()), int(input()), int(input())]
age = (r[0] * 70 + r[1] * 21 + r[2] * 15) % 105

print("Your age is {}; that's a good time to start programming!".format(age))
