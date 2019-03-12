'''
def capitalize(my_name):
    #converts to uppercase
    return my_name.upper()

print(capitalize(input('Type in your name: ')))

def add_two(number):
    #return must be the last number in the function
    return number + 2

print(add_two(int(input('What is your number? '))))

'''


def cap_first_letter(sentence):
    new_sent = ''
    for idx, character in enumerate(sentence):
        if idx == '0':
            new_sent += sentence[idx].upper
        elif character == " ":
            new_sent += character
            new_sent += sentenece[idx + 1].upper()
        elif sentence[idx -1] == " ":
            continue
        else:
            new_sent += character

    return new_sent


print(cap_first_letter(input("Type in your sentence: ")))


