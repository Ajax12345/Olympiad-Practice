x = input()
x = str(x)

counter = 0
for i in x:
    counter += int(i)
print counter

while counter >= 1:
    if counter < 10:
        break
    else:
        counter = str(counter)
        second_count = 0
        for i in counter:
            second_count += int(i)

        print second_count
        counter = second_count
