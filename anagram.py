word = "lepoee"
other_word = "people"

word = list(word)
other_word = list(other_word)

other_word.sort()
word.sort()
if word == other_word:
    print "yes"
else:
    print "no"
