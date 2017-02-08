import random
n = input()
the_matrix = [[] for i in range(n)]
for i in range(n):
    for b in range(n):
        x = random.randint(1, 10)
        the_matrix[i].append(x)


print the_matrix
