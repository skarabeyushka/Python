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
cubes =input("please enter number of cubes to use :\n")
cubes=int(cubes)
steps = solve(1, cubes, 2 * cubes)
if steps != -1:
 steps -= 1

if cubes > 100:

    newcubes = input("please enter number less than 100 :")
    newcubes=int(newcubes)
    steps1 = solve(1, newcubes, 2 * newcubes)
    if steps1 != -1:
        steps1 -= 1

    print("Number of stair steps = ", steps1)

else :
 print("Number of stair steps = ", steps)
