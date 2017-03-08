import random
import string
size = input()
matrix = [["0" for i in range(size)] for i in range(size)]

letters = [i for i in string.ascii_uppercase]

for i in range(size):
    for b in range(size):
        matrix[i][b] = random.choice(letters)
for i in matrix:
    print i
counter = 1

for i in matrix:
    if counter%2 != 0:
        for b in i:
            print b,
        counter += 1

    else:
        for b in range(len(matrix)):
            print i[len(matrix)-b-1],

        counter += 1
