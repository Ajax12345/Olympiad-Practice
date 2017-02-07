from __future__ import print_function
n = 8
word = "TURING"
for i in range(n):
    for b in range(i):

        print(word[b%len(word)], end="")


    print()
