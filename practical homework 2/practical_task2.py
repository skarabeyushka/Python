

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

sum1 = 0

def max(arr,k):


    global sum1
    max1 = arr[0]

    for i in range(0, len(arr)):
        if arr[i] > max1:
            max1 = arr[i]

    if (max1 == k):
        sum1 += 1
        print("k is max in array x")
    else:
        print("k is not max in array x")

sum2 = 0
def checkinarray(arr,k):
 try:
    global sum2
    h = int(len(arr) / 2)

    indice = arr.index(k)

    for i in arr:
        if (i == k):
            print(" k Element Exists in array x")

    if (indice < h):
     sum2 += 1
     print("k is in first part of array x")
    else:
        print("k is not in first part of array x")
 except ValueError:
    print("k is not in the array ")

sum3 = 0
sum = 0

def finalcalculation(arr,arr1,k):
 try:
    global sum3
    global sum
    indice = arr.index(k)

    for i in arr1:
        if (i > 0):
         sum3 += 1

    sum = sum1+sum2

    if (sum == 2 and sum3 == 0):
        print("confitions aligned so array x elements befor k will be rasised to their cube :")
        for i in range(0,indice):
            arr[i] = arr[i] ** 3
    else:
        print("sorry the conditions didnt align so array x dosent change :")

    print("Array x :", arr)
 except ValueError:
     print("k is not in the array so we cannot continue ")




def binary_search(arr, k):
    Noperations = 0
    low = -1
    high = len(arr)
    while high > low+1 :
        Noperations += 4
        print("high > low+1, half = (low + high) // 2")
        half = (low + high) // 2
        if arr[half] >= k:
            print("high = %d low = %d half = %d\narr[half] >= key, high = half"%(high,low,half))
            high = half
        else:
            print("high = %d low = %d half = %d\narr[half] >= key, low = half"%(high,low,half))
            low = half
        print()
    i = high
    indexes = []
    if (i == len(arr) or ((i == 0) and arr[i] != k)):
        print("Element isn't found in the array ")
    else:
        while (True):
            if (arr[i] == k):
                indexes.append(i)
                if (i == len(arr) - 1):
                    break
            else:
                break
            i += 1
        return (indexes, Noperations)



while True:
    print('''welcome user !!!!
    Choose your option: 
    1. Input array elemnets and k 
    2. Exit''')
    userchoice = user_input("your choice")
    if userchoice == 1:
        arr = user_input("arrayinput")
        k = user_input("k")
        print("Array x :", arr)
    else:
        print("thank you for your time!!!!!")
        break

    indexes, Noperations = binary_search(arr, k)
    print("k is at indexes  = ",indexes ,"\n"
          "operations number  is = ",Noperations)






