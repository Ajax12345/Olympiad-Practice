#another version of the Goldbach Conjecture programming problem

the_value = 0
while True:
    the_value = input()
    if the_value%2 == 0:
        break

    else:
        print "Enter again"
        continue


range_primes = [x for x in range(2, the_value) if all(x%y != 0 for y in range(2, x))]

checker_value = 0

for i in range(len(range_primes)):
    checker_value = range_primes[i]
    for b in range_primes:
        if checker_value + b == the_value:
            print str(checker_value)+"+"+str(b)+"="+str(the_value)
