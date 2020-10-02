def numberofvariants(n,max):
    res = 1
    for i in range(n-1,min_at_bottom(n)-1,-1):
        if(i>=max):
            res = 0
            continue
        res+=numberofvariants(n-i,i)
        if((n-i)==i):
            res-=1
    return res

def min_at_bottom(n):
    if(n==1 or n==2):
        return n
    tmp = 0
    for i in range(1,n,1):
        tmp+=i
        if (tmp>=n):
            return i
    return -1


try:
 cubes =input("please enter number of cubes to use :\n")
 cubes = int(cubes)
 if(cubes<100):
     steps = numberofvariants( cubes,  cubes)
     print("Number of stair steps = ", steps)
 if cubes > 100:

   cubes = input("please enter number less than 100 :")
   cubes = int(cubes)
   steps = numberofvariants(cubes,  cubes)
   print("Number of stair steps1 = ", steps)

 if(cubes<0):
     print("please enter positive number")
     cubes = input("please enter number of cubes to use :\n")
     cubes = int(cubes)
     steps = numberofvariants( cubes,  cubes)
     print("Number of stair steps = ", steps)



except ValueError:
 print("enter a number")
 cubes = input("please enter number of cubes to use :\n")
 cubes=int(cubes)
 if (cubes < 0):
     print("please enter positive number")
     cubes = input("please enter number of cubes to use :\n")
     cubes = int(cubes)
     steps = numberofvariants(cubes, cubes)
     print("Number of stair steps = ", steps)
 else:
     steps = numberofvariants( cubes, cubes)
     print("Number of stair steps = ", steps)


















