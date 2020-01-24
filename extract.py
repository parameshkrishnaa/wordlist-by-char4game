import re

words = open("100words.txt", "r")
one = open('1word.txt', 'w')
two = open('2word.txt', 'w')
three = open('3word.txt', 'w')
four = open('4word.txt', 'w')
five = open('5word.txt', 'w')

for word in words:
    if re.match("^[A-z]$", word):
        one.write(word)
    if re.match("^[A-z][A-z]$", word):
        two.write(word)
    if re.match("^[A-z][A-z][A-z]$", word):
        three.write(word)
    if re.match("^[A-z][A-z][A-z][A-z]$", word):
        four.write(word)
    if re.match("^[A-z][A-z][A-z][A-z][A-z]$", word):
        five.write(word)
        #onew.close()
       # print(word)
        #onew.close()
       # print(word)
        #onew.close()
       # print(word)
        #onew.close()
       # print(word)
