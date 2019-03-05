'''
grade = 79

if grade >= 80:
    print("A")
elif grade >=60:
    print("B")
else:
    print("C")
'''

from random import randint
answer = randint(1, 10)
guess = int(input("Please enter your guess: "))

#print(type(guess))

if guess == answer:
    print("Correct")
else:
    print("Try again")
    print(f'Answer was:{answer}')