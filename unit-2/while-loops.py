''''
#print a message 10 times
count = 0
while count < 10:
    print("Inside the while loop")
    count += 1

#search for value in list
nums = [2, 8, 22, 34, 72, 42, 62]
found = False
key = 22
for idx, item in enumerate(nums):
    print(idx, item)
    if nums[idx] == key:
        break


#continue

my_nums = [1, 3, 15, 8, 7, 24, 6, 5, -1]

for num in my_nums:
    if num % 2 == 0:
        continue
    print(f'{num} is odd!')


answer = 27
user_input = None
while answer != user_input:
    user_input = int(input("Please input an integer: "))

    if answer < user_input:
        print("Too big")
        print("Play again")
    elif answer > user_input:
        print("Too small")
        print("Play again")
    elif answer == user_input:
        print("You got it!")
        break
'''

#find sum of a list of numbers
ages = [25, 39, 45, 41, 27, 18, 33, 65, 11, 50]
sum = 0
for num in ages:
    sum += num

print(sum)