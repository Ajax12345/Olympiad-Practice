while True:
    c = input()
    if c%2 == 0:
        break

    else:
        print "Sorry, that number is not even, please enter again: "
        continue




the_primes = [x for x in range(2, c)
     if all(x % y != 0 for y in range(2, x))]

result = []
for i in the_primes:
    new_value = c - i
    if new_value in the_primes:
        result.append(str(new_value)+ "+"+ str(i)+ "= "+ str(c))

import random

print random.choice(result)
