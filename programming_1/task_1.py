limit = int(input("enter upper limit for perfect number search: "))

n = 1

while n <= limit:

    sum = 0
    divisor = 1
    while divisor < n:
        if not n % divisor:
            sum += divisor
        divisor = divisor + 1
    if sum == n:
        print(n, "is a perfect number")
    n = n + 1
