'''
#my_list = []
#my_list.append()
#my_list.insert(idx,"")
#my_list.pop()
#my_list.remove(idx)

#Lists are both ordered and mutable
#dictionaries:a collection of keyvalue pairs
students = {}
#add to dictionary
students['name'] = 'John'
print(students)
students['name'] = 'Martha'
print(students)

course_list = ['Python programming', 'Data Science', 'UX', 'Social Media Marketing']
students['courses'] = course_list
print(students)

course_list.append('Web Development')
print(students)
'''
#model playlist
#each song has:
#genre - could be a list
#artist - could be a list
#album - string
#release year - string
#name - string
#playback_length - string
#basically a dictionary
'''
my_playlist = []
song1 = {'name': 'Unsteady', 'artist': 'X Ambassadors', 'album': 'VHS', 'year': '2017','genre': 'Alternative', 'length': '3:26'}
my_playlist.append(song1)

print(my_playlist)

##play list info

name = ''
genres = []
artists = []
album = ''
release year = ''
playback_length = ''

number_of_songs = input()
while i <= number_of songs:
    name = input("What is the name of your song: ")
    genres[0] = input("What is the genre of your song: ")


def swap_first_two(my_list):
    temp = my_list[0]
    my_list[0] = my_list[1]
    my_list[1] = temp
    return my_list

a_list = [1,2,15,20]

print(swap_first_two(a_list))

my_string = 'Apple'

def change_string(a_string):
    list(a_string)
    a_string = 'Orange'
    return a_string


#change_string(my_string)
change_string(my_string)
print(my_string)

my_name = {'c':2,'a':2,'l':1,'r':1,'o':1}

for key,num in my_name.items:
    print(f'The letter {key} appears {num} times in your name')

def frequency_generator(a_string):
    a_string.slice(" ")
'''

word_dictionary = {}
my_sentence = 'There is a man with a plan. the man has a plan in hand'

def word_counter(sentence):
    x = 0
    split = sentence.split(" ")
    while x < len(split):
        if "." in split[x]:
            split[x] = split[x].replace(".", "")

        if split[x] in word_dictionary.keys():
            word_dictionary[split[x]] += 1
        else:
            word_dictionary[split[x]] = 1
        x+=1
    for key, value in word_dictionary.items():
        print(key + ": " + str(value))

word_counter(my_sentence)

