f = open("first.txt").readlines()

f = [i.strip('\n') for i in f]
new_list = []
for i in f:
    new_list.append(i.split(' '))
second_list = []
for i in new_list:
    second_list.append(map(int, i))

#print second_list

n = second_list[0][0]
queens_position = second_list[1]
second_list.remove(second_list[0])
second_list.remove(second_list[0])
#print second_list
#print queens_position
queens_range = []
horizontal = []
vertical = []
diagonal_positive = []
diagonal_negative = []
for i in range(n):
    if i < queens_position[0]:
        horizontal.append([queens_position[0]-i, queens_position[1]])

    else:
        horizontal.append([queens_position[0]+(queens_position[0]-i+1), queens_position[1]])

for i in range(n):
    if queens_position[0]+ i < n:
        diagonal_positive.append([queens_position[0]+i+1, queens_position[1]+i+1])
    else:
        diagonal_positive.append([abs(i-queens_position[0]), abs(i-queens_position[1])])


for i in diagonal_positive:
    if i[0] == 0:
        diagonal_positive.remove(i)


for i in range(n):
    if queens_position[0] + i <= n: #<=n
        diagonal_negative.append([queens_position[0]+i, queens_position[1]-i])

        diagonal_negative.append([queens_position[0]-i, queens_position[1]+i])

    elif queens_position[1] + i <= n:
        diagonal_negative.append([abs(i-queens_position[0]), queens_position[1]+1])
        
 '''
5 3
4 3
5 5
4 2
2 3
'''
