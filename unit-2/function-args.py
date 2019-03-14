#function that returns the sum of
#any number of numbers passed in
'''
def add(*args):
    sum = 0
    for val in args:
        sum += val
    return sum

print(add(1, 2))


#message('Bob, 'Python')
# hello Bob, you're doing Python!!

def message(*args):
    name = args[0]
    message1 = f'Hello {name}'
    if len(args) == 1:
        print(message1)
    elif len(args) == 2:
        occupation = args[1]
        message2 = f', you\'re doing {occupation}'
        print(message1 + message2)
    else:
        pass

message('Joseph', 'Python')
message('Alice', 'UI Design')
message('Charlie', 'Web Dev')
message('May', 'nothing, get to work')
message('John')



#Keyword arguments
#print('This', 'is', 'an', 'awesome', 'Python', 'course', sep='--')

def say_hi(name, job='Instructor'):
    print(f'Hello {name}, you\'re an {job}')

say_hi('Marcus','Developer')


def say_hello(**kwargs):
    #hello name, it's great that you're a job
    vowels = ['A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u']
    for key, val in kwargs.items():
        if val[0] in vowels:
            print(f'Hello {key}, it\'s great that you\'re an {val}')
        else:
            print(f'Hello {key}, it\'s great that you\'re a {val}')

say_hello(Bob='Engineer', Alice='Lawyer')
#people = {'Bob': 'Engineer', 'Alice': 'Lawyer'}
#print(people)
#print(people.keys())
#print(people.values())
#print(people.items())

'''

def car_type(**kwargs):
    #car_type(make='Subaru', colour='black')
    #print(len(kwargs))
    if len(kwargs) == 2:
        model = kwargs['make']
        col = kwargs['colour']
        print(f'Your {model} is {col}, that\'s so cool')
    elif len(kwargs) == 3:
        year = kwargs['year']
        model = kwargs['make']
        col = kwargs['colour']
        print(f'Your {year} {model} is {col}, that\'s so cool')
car_type(year='2017', make='Subaru', colour='black')




