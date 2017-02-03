f = open("first.txt").readlines()
f = [i.strip('\n') for i in f]
new_list = []
for i in f:
    new_list.append(i.split(' '))

second_list = []
for i in new_list:
    second_list.append(map(int, i))



the_first_corrindate = [second_list[0][0], second_list[0][1]]
the_second_corrindate = [second_list[1][0], second_list[1][1]]
corrdinates_1 = [the_first_corrindate, [second_list[0][0]+second_list[0][2], second_list[0][1]], [second_list[0][0], second_list[0][1]-second_list[0][3]], [second_list[0][0]+second_list[0][2], second_list[0][1]-second_list[0][3]]]
corrdinates_2 = [the_second_corrindate, [second_list[1][0]+second_list[1][2], second_list[1][1]], [second_list[1][0], second_list[1][1]-second_list[1][3]], [second_list[1][0]+second_list[1][2], second_list[1][1]-second_list[1][3]]]
flag = False
for i in corrdinates_1:
    for b in corrdinates_2:
        if (abs(i[0]) >= abs(b[0]) and abs(i[1]) >= abs(b[1])):
            flag = True
            break

        else:
            flag = False
            continue

if flag:
    print "They overlap or touch"

else:
    print "They do not overlap"

print corrdinates_1
print corrdinates_2

'''
Sample input:

0 1 1 1
3 3 1 1

x, y, w, h
