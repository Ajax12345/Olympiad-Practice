def main():
    f = open('first.txt')
    the_list = []
    for i in f:
        the_list.append(int(i))

    for i in the_list:
        if i == 0:
            print "zero"

        elif i >= 0 and i < 10:
            print ten_to_the_0(i)

        elif i >= 10 and i < 20:
            print ten_to_the_one(i)

        elif i >= 20 and i < 100:
            the_list = [int(b) for b in str(i)]

            print ten_to_the_one1(the_list[0])+" "+ten_to_the_0(the_list[1], " ")

        elif i >= 100 and i < 1000:
            the_list = [int(b) for b in str(i)]
            if the_list[1] == 0:
                print ten_to_the_0(the_list[0], " ") + " "+ "hundred" + ten_to_the_0(the_list[2], " ")

            else:
                print ten_to_the_0(the_list[0], " ") + " "+ "hundred" + ten_to_the_one(int(str(the_list[1])+str(the_list[2])))

        elif i >= 1000 and i < 10000:


            the_list = [int(b) for b in str(i)]
            if the_list[2] == 1:
                print ten_to_the_0(the_list[0], " ") + " "+ "thousand"+ ten_to_the_0(the_list[1], "hundred") + ten_to_the_one(int(str(the_list[2])+str(the_list[3])))

            else:
                print ten_to_the_0(the_list[0], " ") + " "+ "thousand"+ ten_to_the_0(the_list[1], "hundred") + ten_to_the_one1(the_list[2]) + " " +ten_to_the_0(the_list[3], " ")

        elif i >= 10000 and i < 100000:
            the_list = [int(b) for b in str(i)]
            if int(str(the_list[0])+str(the_list[2])) >= 10 and int(str(the_list[0])+str(the_list[2])) <= 20:
                print ten_to_the_one(int(str(the_list[0])+str(the_list[2])))+ " thousand"+ ten_to_the_0(the_list[1], "hundred") +




def ten_to_the_0(number, trailing):
    if number == 0:
        return " "

    the_letters = {1:"one", 2:"two", 3:"three", 4:"four", 5:"five", 6:"six", 7:"seven", 8:"eight", 9:"nine"}
    return the_letters[number] + trailing

def ten_to_the_one(number):

    if number == 10:
        return "ten "

    elif number == 0:
        return " "

    elif number == 11:
        return "eleven "

    elif number == 12:
        return "twelve "

    elif number == 13:
        return "thirteen "

    elif number == 14:
        return "fourteen "

    elif number == 15:
        return "fifteen "

    elif number == 16:
        return "sixteen "

    elif number == 17:
        return "seventeen "

    elif number == 18:
        return "eighteen "

    elif number == 19:
        return "nineteen "

def ten_to_the_one1(number):
    if number == 2:
        return "twenty "

    elif number == 0:
        return " "

    elif number == 3:
        return "thirty "

    elif number == 4:
        return "forty"

    elif number == 5:
        return "fifty "

    elif number == 6:
        return "sixty "

    elif number == 7:
        return "seventy "

    elif number == 8:
        return "eighty "

    elif number == 9:
        return "ninety "

main()
