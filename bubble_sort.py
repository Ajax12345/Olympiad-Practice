the_list = [4, 5, 2, 3, 5]


for i in range(len(the_list)):
    for b in range(len(the_list)):
        if the_list[b] < the_list[i]:
            first_value = the_list[b]
            second_value = the_list[i]
            the_list[i] = first_value
            the_list[b] = second_value



new_list = []

for i in range(len(the_list)):
    new_list.append(the_list[len(the_list)-1-i])

print new_list
