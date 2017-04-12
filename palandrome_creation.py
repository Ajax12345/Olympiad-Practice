from string import ascii_lowercase
string = "cbadefg"
#string2 = string[::-1]
string2 = string[::-1]
counter = 0

if string == string[::-1]:
    counter = 0


else:
    letters = [i for i in ascii_lowercase]
    alphabet = {letters[i+1]:letters[i] for i in range(len(letters)) if i+1 < len(letters)-1}
    new_alphabet = {letters[i]:letters[i+1] for i in range(len(letters)) if i+1< len(letters)-1}

    for i in range(len(string)):
        value1 = string2[i]
        value2 = string[i]

        while value1 != value2:
            if value1 < value2:

                value1 = new_alphabet[value1]
                counter += 1
            else:
                value1 = alphabet[value1]
                counter += 1




print counter
