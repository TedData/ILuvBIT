def add(n,m):
    """ Adds two numbers together and returns the result"""
    return n+m

num1 = input("Enter first number: ")
num2 = input("Enter second number: ")

try :
    result = add(int(num1), int(num2))
    print(result)
except ValueError:
    print("Invalid number entered")
