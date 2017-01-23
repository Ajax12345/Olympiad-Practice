def main():
    f = open('first.txt').readlines()
    f = [i.strip('\n') for i in f]
    new_list = []
    for i in f:
        new_list.append(i.split(' '))

    second_list = []
    for i in new_list:
        second_list.append(map(int, i))


    gcf = []
    for i in range(len(second_list)):
        the_gcf = is_gcf(second_list[i][0], second_list[i][1])
        gcf.append(the_gcf)


    print gcf

def is_gcf(number1, number2):
    the_list = []
    maximum = 0
    for i in range(1, number1+1):
        if number2%i == 0 and number1%i == 0:
            the_list.append(i)

    if len(the_list) == 1:
        return 1

    else:
        for i in the_list:
            if i > maximum:
                maximum = i

        return maximum


main()
