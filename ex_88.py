my_string = input('Enter a string: ')
new_string = ''
new_string += my_string[0].upper()
i = 1

while i < len(my_string)-2:
    new_string += my_string[i]
    if my_string[i] == '.' or my_string[i] == '?' or my_string[i] == '!':
        new_string += ' '
        new_string += my_string[i+2].upper()
        i = i+3
    else:
        if i == len(my_string)-3:
            new_string += my_string[len(my_string)-2:len(my_string)]
        i = i+1

print(new_string)