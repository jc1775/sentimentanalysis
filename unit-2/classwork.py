
#Creates a list
classmates = ["Ros", "Marcus", "Flavio", "Joseph", "Maham", "Vinay", "Gungeet", "Faris"]

'''''
#Finds and prints number of items in the list
num_classmates = len(classmates)
print(num_classmates)

#Accessing information from a list AKA indexing
#Prints the first
print(classmates[0])

#Prints the last
print(classmates[-1])

#Adds element to end of list
classmates.append("John")
print(classmates[-1])

#Inserting elements
classmates.insert(1, "Jane")
print(classmates[1])

#Removing from end
classmates.pop()
#or remove from specific spot
classmates.pop(1)

#print all elements
for name in classmates:
    print(name)


#Search for item in list
username = input()
for name in classmates:
    if username == name:
        print(f'{username} was found in the list')


username = input()
if username in classmates:
    print(f'{username} is in the list')
else:
    print(f'{username} is not in the class')

#Enumerate function -- Using indices in for loop

for idx, name in enumerate(classmates):
    print(idx + 1, name)

#Printing backwards

name = "Joseph"
for x in range(len(name) -1, -1, -1):
    print(name[x])
'''''

#Shortest way
name = "Joseph"
print(name[::-1])
print(name[:3:-1])

