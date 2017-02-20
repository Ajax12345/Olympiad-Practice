the_numbers = [15, 1, 7, 2]

first_side = [the_numbers[0], the_numbers[1]]

second_side = [the_numbers[2], the_numbers[3]]

operators1= [0, 0, 0, 0]

operators2 = [0, 0, 0, 0]

operators1[0] = first_side[0] + first_side[1]

operators1[1] = first_side[0] - first_side[1]

operators1[2] = first_side[0]*first_side[1]

operators1[3] = first_side[0]/first_side[1]

operators2[0] = second_side[0] + second_side[1]

operators2[1] = second_side[0] - second_side[1]

operators2[2] = second_side[0]*second_side[1]

operators2[3] = second_side[0]/second_side[1]


for i in operators1:
    if i in operators2:
        the_first_number = [c for c, a in enumerate(operators1) if a == i]
        the_second_number = [b for b, x in enumerate(operators2) if x == i]


        if the_first_number[0] == 0:
            if the_second_number[0] == 0:
                print str(first_side[0])+"+"+str(first_side[1])+"="+str(second_side[0])+"+"+str(second_side[1])


            elif the_second_number[0] == 1:
                print str(first_side[0])+"+"+str(first_side[1])+"="+str(second_side[0])+"-"+str(second_side[1])

            elif the_second_number[0] == 2:
                print str(first_side[0])+"+"+str(first_side[1])+"="+str(second_side[0])+"*"+str(second_side[1])

            elif the_second_number[0] == 3:
                print str(first_side[0])+"+"+str(first_side[1])+"="+str(second_side[0])+"/"+str(second_side[1])


        elif the_first_number[0] == 1:
            if the_second_number[0] == 0:
                print str(first_side[0])+"-"+str(first_side[1])+"="+str(second_side[0])+"+"+str(second_side[1])

            elif the_second_number[0] == 1:
                print str(first_side[0])+"-"+str(first_side[1])+"="+str(second_side[0])+"-"+str(second_side[1])

            elif the_second_number[0] == 2:
                print str(first_side[0])+"-"+str(first_side[1])+"="+str(second_side[0])+"*"+str(second_side[1])

            elif the_second_number[0] == 3:
                print str(first_side[0])+"-"+str(first_side[1])+"="+str(second_side[0])+"/"+str(second_side[1])


        elif the_first_number[0] == 2:
            if the_second_number[0] == 0:
                print str(first_side[0])+"*"+str(first_side[1])+"="+str(second_side[0])+"+"+str(second_side[1])

            elif the_second_number[0] == 1:
                print str(first_side[0])+"*"+str(first_side[1])+"="+str(second_side[0])+"-"+str(second_side[1])

            elif the_second_number[0] == 2:
                print str(first_side[0])+"*"+str(first_side[1])+"="+str(second_side[0])+"*"+str(second_side[1])

            elif the_second_number[0] == 3:
                print str(first_side[0])+"*"+str(first_side[1])+"="+str(second_side[0])+"/"+str(second_side[1])


        elif the_first_number[0] == 3:
            if the_second_number[0] == 0:
                print str(first_side[0])+"/"+str(first_side[1])+"="+str(second_side[0])+"+"+str(second_side[1])

            elif the_second_number[0] == 1:
                print str(first_side[0])+"/"+str(first_side[1])+"="+str(second_side[0])+"-"+str(second_side[1])

            elif the_second_number[0] == 2:
                print str(first_side[0])+"/"+str(first_side[1])+"="+str(second_side[0])+"*"+str(second_side[1])

            elif the_second_number[0] == 3:
                print str(first_side[0])+"/"+str(first_side[1])+"="+str(second_side[0])+"/"+str(second_side[1])
