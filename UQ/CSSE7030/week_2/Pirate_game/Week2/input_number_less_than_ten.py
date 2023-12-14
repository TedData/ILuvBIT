#
# Program to input a number between 0 and 10
#
test=float(input('Input a number less than 10:'))
while test >= 10:
    test=float(input("Number not valid. Try again:"))
print('The number is', test)
