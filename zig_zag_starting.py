#this is the start of my matrix zigzag algorithm, as of 3/6/17 it is a work in progress

import random

size = random.randint(2, 7)

matrix = [[random.randint(1, 100) for i in range(size)] for b in range(size)]
for i in matrix:
    print i
print matrix[0][0],
for i in range(len(matrix)):
    for b in range(len(matrix)):
        if i < len(matrix)-1 and b > 0:

            print matrix[i][b],

            print matrix[i+1][b-1],
print matrix[len(matrix)-1][len(matrix)-1]
