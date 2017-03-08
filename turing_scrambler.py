import random

my_string = "TURING"
print my_string
new_word = []
for i in range(len(my_string)):
    the_key = random.randint(0, len(my_string)-1)
    new_word.append(my_string[the_key])
counter = 0
second_word = ''.join(new_word)
print second_word
for i in range(len(my_string)):
    if my_string[i] == second_word[i]:
        counter += 1

print counter
