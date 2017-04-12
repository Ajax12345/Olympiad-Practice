def main():
    string = "one hundred thousand fifty six"
    lst = string.split()

    answer = []

    for i in lst:
        answer.append(converter(i))

    final_answer = ''
    for i in range(len(answer)):
        if i+1 < len(answer):
            first = answer[i]
            second = answer[i+1]

            if len(answer[i]) < len(answer[i+1]):
                the_sum = ''
                the_sum += first+second
                if len(final_answer) < len(the_sum):
                    final_answer += the_sum

                else:
                    final_answer = final_answer[:len(the_sum)]+the_sum

            else:

                final_answer = final_answer[:len(first[:len(second)]+second)-1] + first[:len(second)]+second




    print final_answer



def converter(letter):
    dct = {"one":"1", "two":"2", "three":'3', "four":'4', 'five':'5', 'six':'6', 'seven':'7', 'eight':'8', 'nine':'9', 'ten':'10',
    'eleven':'11', 'twelve':'12', 'thirteen':'13', 'fourteen':'14', 'fifteen':'15', 'sixteen':'16', 'seventeen':'17', 'eighteen':'18', 'nineteen':'19', 'twenty':'20', 'thirty':'30',
    'fourty':'40', 'fifty':'50', 'sixty':'60', 'seventy':'70', 'eighty':'80', 'ninety':'90', 'hundred':'00', 'thousand':'000', 'million':'000000'}

    return dct[letter]

main()
