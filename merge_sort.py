theList = [6, 3, 4, 5, 7]

for i in range(0, len(theList), 2):
    if i < len(theList)-1:
        value1 = theList[i]
        value2 = theList[i+1]
        if theList[i] > theList[i+1]:
            theList[i] = value2
            theList[i+1] = value1

for i in range(1, len(theList)):
    if i < len(theList)-1:
        value1 = theList[i]
        value2 = theList[i+1]
        if theList[i] > theList[i+1]:
            theList[i] = value2
            theList[i+1] = value1


print theList
