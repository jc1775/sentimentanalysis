sentence = input('Enter a sentence: ')
new_str = ''
last_let = len(sentence) - 1

while last_let >= 0:
    new_str += sentence[last_let]
    last_let -= 1
print(new_str)
#Takes two strings and joins them together
print(''.join(reversed(sentence)))