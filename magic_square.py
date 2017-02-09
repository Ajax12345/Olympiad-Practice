the_square = [[7,3,5],[6,8,1],[2,4,9]]
count1 = 0
second_count = 0
the_sides = []
for i in range(len(the_square)):
    for b in range(len(the_square)):
        count1 += the_square[i][b]
    the_sides.append(count1)
    count1 = 0

for i in range(len(the_square)):
    for b in range(len(the_square)):
        second_count += the_square[b][i]

    the_sides.append(second_count)

    second_count = 0


if len(list(set(the_sides))) == 1:
    print "It is a magic square"

else:
    print "It is not magic square"
