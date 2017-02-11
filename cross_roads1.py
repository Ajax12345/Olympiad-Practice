f = open('crossroad.in').readlines()
f = [i.strip('\n') for i in f]
output_file = open('crossroad.out', 'w')
d = str(f[0])

f.remove(d)


second_list = []

for i in f:
    second_list.append(i.split(' '))
third_list = []
for i in second_list:
    third_list.append(map(int, i))



ids = []
bools = []

the_dictoniary = {}

for i in third_list:
    ids.append(i[0])
    bools.append(i[1])

for i in range(len(ids)):
    if ids[i] not in the_dictoniary:
        the_dictoniary[ids[i]] = [bools[i]]

    else:
        the_dictoniary[ids[i]].append(bools[i])



count = 0
ids = list(set(ids))
for i in ids:
    while True:
        if len(the_dictoniary[i]) == 1 or len(the_dictoniary[i]) == 0:
            break

        else:
            if 1 and 0 in the_dictoniary[i]:
                count += 1

                the_dictoniary[i].remove(1)
                the_dictoniary[i].remove(0)

                continue



output_file.write(str(count))

output_file.close()
