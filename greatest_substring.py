#this problem finds the greatest substring that exists in two given strings

def main():
    string1 = "abaabcd"
    string2 = "aaacvebaabcda"
    tack_on_string = ''
    the_substrings = []
    for i in range(len(string1)):
        string1 = string1[i:len(string1)+1]
        for i in string1:

            if string2.count(tack_on_string+i) > 0:
                tack_on_string += i
                continue

            else:
                break

        the_substrings.append(tack_on_string)
        tack_on_string = ''


    print max(the_substrings, key=len)

main()
