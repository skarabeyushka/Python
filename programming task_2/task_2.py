from random import randint

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

def checkinarray(arr,k,arr1):
    sum1,sum2,sum3=0,0,0
    max = arr[0]

    for i in range(0, len(arr)):
        if arr[i] > max:
            max = arr[i]

    if (max == k):
        sum1+=1
        print("k is max in array x")
    else:
        print("k is not max in array x")


    indice= arr.index(k)
    h=int(len(arr)/2)
    if(indice<h):
        sum2+=1
        print("k is in first part of array x")
    else:
        print("k is not in first part of array x")

    for i in arr1: 
        if (i > 0):
         sum3+=1


    sum=sum1+sum2
    if (sum == 2 and sum3 == 0):
        print("confitions aligned so array x elements befor k will be rasised to their cube :")
        for i in range(0,indice):
            arr[i] = arr[i] ** 3
    else:
        print("sorry the conditions didnt align so array x dosent change :")

    print("Array x :", arr)

while True:
    print('''welcome user !!!!
    Choose your option: 
    1. Input array elemnets and k 
    2. Input n, k and the array will be generated randomly
    3. Exit''')
    userchoice = user_input("your choice")
    if userchoice == 1:
        arr = user_input("arrayinput")
        arr1= user_input("arrayinput")
        k = user_input("k")
        print("Array x :", arr)
        print("Array y :", arr1)
    elif userchoice == 2:
        n = user_input("n")
        print("You need to input a i b for range of elements: ")
        a = user_input("a")
        b = user_input("b")
        k = user_input("k")
        arr = [randint(a, b) for i in range(n)]
        arr1 = [randint(a, b) for i in range(n)]
        print("Array x :", arr)
        print("Array y :", arr1)
    else:
        print("thank you for your time!!!!!")
        break

    checkinarray(arr,k,arr1)

































