#!/usr/python3
base = ""
# user inputs base
base = input("what is the base? ")
# base is converted to an integer by basenum
basenum = int(base)
# what is the decimal number
number = input("what is your number? ")
tempnumb = int(number)
tempout = ""
# convert the decimal to the base selected 
while(tempnumb > 0):
    #defines tempout as tempnum modulo basenum
    tempout = str(tempnumb % basenum) + tempout
    # this line sets "tempnumb" to an integer that is the input integer divided by the variable basenum
    tempnumb = int(tempnumb / basenum)
# print the result
print(tempout)
