"""
Program name : Wk5_Ryan_Rotthoff.py
Student Name :Ryan Rotthoff
Course : ENTD220
Instructor : Georgia Brown
Date : 5/9/2021
Copy Wrong : This is my work
"""

# This program will improve on the calculator program by using modules
# and string manipulation.


# Define IsinRange function
def IsinRange():
    lr = lowrange
    hr = highrange
    n = num1 and num2
    if lr < n and n < hr:
        return True
    else:
        return False

# import Mylib module for calculator operations

import Mylib
n=Mylib.add(x,y)
        print(n)

# excpetion handling using try/except to catch ValueError       

while True:
    lowrange = input("Enter Lowest range: ")
    try:
        lowrange = float(lowrange)
    except ValueError:
        print("Must enter an integer")
        print("Calculator Off!")
        exit()
    if lowrange < -100:
        try:
            print("Low range limit is -100")
            print("Calculator Off")
            exit()
        except ValueError:
            print("Must enter an integer")
            exit()

    highrange = input("Enter higher range: ")
    try:
        highrange = float(highrange)
    except ValueError:
        print("Must enter an integer")
        print("Calculator Off")
        exit()
    if highrange> 100:
        try:
            print("High range limit is 100")
            exit()
        except ValueError:
            print("Must enter an integer")
            print("Calculator Off")
            exit()
    while True:
        num1 = input("First number? ")
        try:      
            num1 = float(num1)
        except ValueError:
            print("Must enter an integer")
            print("Calculator Off")
            exit()
        num2 = input("Second number? ")
        try:
            num2 = float(num2)
        except ValueError:
            print("Must use integer")
            print("Calculator off")
            exit()

        if IsinRange() is False:
            try:
                print("Enter a valid number between",lowrange ,"and", highrange,", Please check the number and try again")
                print("Calculator Off")
                exit()
            except TypeError:
                print("Must use integer")
                exit()
            except ValueError:
                print("Must use integer")
                exit()
        else:
            break

    # User input for math operations


    print("The Result of",num1,"+", num2,"=",add(num1,num2))
    print("The Result of",num1,"-", num2,"=",subtract(num1,num2))
    print("The Result of",num1,"*", num2,"=",multiply(num1,num2))
    
    # Error "ZeroDivisionError" to show that there was a division that happen
    
    try:
        print("The Result of",num1,"/", num2,"=",divide(num1,num2))
    except ZeroDivisionError:
        print("The Result of",num1,"/", num2,"= Cannot Divide by Zero")
    
    # option to continue
    keepGoing = input("Would you like to continue, Y/N?: ")

    if keepGoing == "Y":
        continue
    elif keepGoing == "N":
        print("Calculator Off")
        exit()
    else:
        print("Please, type 'Y' or 'N'")
        exit()
