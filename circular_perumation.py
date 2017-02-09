#creates a list as [0, 1, 3, 4, 5,..., n]
#prints out a matrix like this:
'''
0 1 2 3 4 5
1 2 3 4 5 0
2 3 4 5 0 1
3 4 5 0 1 2
4 5 0 1 2 3
5 0 1 2 3 4

'''


n = input("Enter the number: ")

first_list = [i for i in range(n)]

for i in range(n):
    for b in range(n):
        print first_list[(b+i)%n],

    print
