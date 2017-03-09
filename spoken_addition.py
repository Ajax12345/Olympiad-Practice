command = "How much is four and six and eleven and twenty one and one hundred?"

new_command = command.split()



removable_phrases = ["How", "much", "is", "and"]

counter = 0
for i in new_command:
    if i == "and":
        counter += 1
for i in range(counter):
    for i in removable_phrases:
        if i in new_command:
            new_command.remove(i)


last_value = new_command[len(new_command)-1]

new_command.remove(last_value)
last_value = last_value.strip("?")
new_command.append(last_value)

print new_command


numerals = [i for i in range(100)]

numbers = {"one":1, "two":2, "three":3, "four":4, "five":5, "six":6, "seven":7, "eight":8, "nine":9}

numbers10 = {"ten":10, "eleven":11, "twelve":12, "thirteen":13, "fourteen":14, "fifteen":15, "sixteen":16, "seventeen":17, "eighteen":18, "ninteen":19, "twenty":20,
            "thirty":30, "fourty":40, "fifty":50, "sixty":60, "seventy":70, "eighty":80, "ninety":90}

numbers100 = {"hundred":"00", "thousand":"000"}

the_sum = 0

sum_list = []
if "hundred" in new_command:
    for i in range(len(new_command)):
        if new_command[i] == "hundred":
            if new_command[i-1] in numbers:
                the_number = str(numbers[new_command[i-1]])+"00"
                sum_list.append(int(the_number))
        elif new_command[i] == "thousand":
            if new_command[i-1] in numbers:
                the_number = str(numbers[new_command[i-1]])+"000"
                sum_list.append(int(the_number))

            elif new_command[i-1] in numbers10:
                the_number = str(numbers10[new_command[i-1]])+"000"
                sum_list.append(int(the_number))

        else:
            if new_command[i] in numbers:
                sum_list.append(numbers[new_command[i]])

            elif new_command[i] in numbers10:
                sum_list.append(numbers10[new_command[i]])


    print sum_list
    print sum(sum_list)


else:
    for i in new_command:
        if i in numbers:
            the_sum += numbers[i]

        elif i in numbers10:
            the_sum += numbers10[i]

    print the_sum
