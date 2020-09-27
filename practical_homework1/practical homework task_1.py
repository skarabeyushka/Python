def solve(low, high, cubes):
    while low <= high:
        mid = int((low + high) / 2)


        if (mid * (mid + 1)) == cubes:
            return mid


        if (mid > 0 and (mid * (mid + 1)) > cubes
                and (mid * (mid - 1)) <= cubes):
            return mid - 1


        if (mid * (mid + 1)) > cubes:
            high = mid - 1;


        else:
            low = mid + 1
    return -1

try:
 cubes =input("please enter number of cubes to use :\n")
 cubes = int(cubes)
except ValueError:
 print("enter a number")
 cubes = input("please enter number of cubes to use :\n")
 cubes=int(cubes)


 if cubes > 100:

    newcubes = input("please enter number less than 100 :")
    newcubes=int(newcubes)
    steps1 = solve(1, newcubes, 2 * newcubes)
    print("Number of stair steps = ", steps1)

 else :
     steps = solve(1, cubes, 2 * cubes)
     print("Number of stair steps = ", steps)

















