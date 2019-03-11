method = input('What method would you like to do? ')
num_1 = int(input('What is your first number? '))
num_2 = int(input('What is your second number? '))
if method == 'add':
    solved = f'Your result is {num_1 + num_2}. Calc you later!'
elif method == 'sub':
    solved = f'Your result is {num_1 - num_2}. Calc you later!'
elif method == 'div':
    solved = f'Your result is {num_1 / num_2}. Calc you later!'
elif method == 'mult':
    solved = f'Your result is {num_1 * num_2}. Calc you later!'

print(solved)