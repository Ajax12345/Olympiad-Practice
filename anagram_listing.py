from math import factorial
string = "abcd"

the_list = list(string)
new_list = []
counter = 0 #this counter tells us how many times the loop should run.
flag = True #need this flag to tell us whether or not to switch the last two or last three
loop_time = factorial(len(the_list))/len(the_list)

for i in range(len(the_list)):
    popped = the_list.pop() #pop off the last

    new_list.append(popped)
    for i in range(loop_time):

        if flag:
            new_list.append(the_list[0])
            part = the_list[1:][::-1]

            new_list.extend(part)
            flag = False

        else:
            new_list.extend(the_list[::-1])
            flag = True
        print ''.join(new_list)
        counter += 1
        the_list = new_list

        new_list = []

print counter
