import random
the_list = []
for i in range(5):
    x = random.randint(10, 100)
    the_list.append(x)
maximum = 0
for i in the_list:
    if i > maximum:
        maximum = i

minimum = maximum
for i in the_list:
    if i < minimum:
        minimum = i
print the_list
print minimum
the_list.remove(minimum)
print the_list


for i in the_list:
    if i < maximum:
        maximum = i

print maximum
