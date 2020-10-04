from itertools import repeat

def user_input(givenchoice):
    while True:
        try:
            if givenchoice == "arrayinput":
                given = [int(i) for i in input("Input array elements : ").split()]

            else:
                given = int(input('Input ' + givenchoice + ': '))

        except ValueError:
            print("please enter a valid number ")
        else:
            return given

def matrix (n):
    A_tup  = [[1,2,n-1,n],
       [n,n-1,2,1]]
    k = int(n/2)
    res = tuple(repeat(A_tup, k))
    print(res)

while True:
    print('''welcome user !!!!
    Choose your option: 
    1. Input n for the matrix
    2. Exit''')
    userchoice = user_input("your choice")
    if userchoice == 1:
        n = int(input('enter n for the matrix : '))
        if(n % 2 )!=0:
            n = int(input('enter a pair number please : '))
        else:
            print("you entered a pair number good job !!")



    else:
        print("thank you for your time!!!!!")
        break


    matrix(n)




















