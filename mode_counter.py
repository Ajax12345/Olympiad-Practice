the_list = [5, 6, 2, 4, 4, 4, 5, 5, 5]

while len(the_list) != 1:
    the_new_list = list(set(the_list))
    for i in the_new_list:
        the_list.remove(i)

print the_list[0]
