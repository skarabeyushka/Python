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
cubes =input("please enter number of cubes less than 100 to use :\n")
cubes=int(cubes)
steps = solve(1, cubes, 2 * cubes)
if steps != -1:
    steps -= 1
print("Number of stair steps = ", steps)