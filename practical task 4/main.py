from iteratorandgenerator import generator
from iteratorandgenerator import Number_it
from functions import finding_is_perfect

class Negative(Exception):
    pass

def validation_input(parametr):
    while True:
        try:
            param = int(input("Enter " + parametr + ": "))
            if parametr == "your choice":
                if param < 0:
                    raise Negative
        except ValueError:
            print("It's not a number")
        except Negative:
            print(parametr + " should be positive")
        else:
            return param




while True:
    print('''welcome user !!!!
    Choose your option: 
    1. Iterator 
    2. Generator
    3. Exit''')
    userchoice = validation_input("your choice")
    if userchoice == 1:

        n = int(input(print(" enter n value : ")))
        values = Number_it(n)


        print("the numbers are : ")
        for i in values:
           finding_is_perfect(i)


    elif userchoice == 2:
        n = int(input(print("enter n value :")))
        values = generator(n)
        print("the numbers are : ")
        for i in values:
            finding_is_perfect(i)
    else:
        print("thank you for your time!!!!!")
        break