def factorial(n):
    if n == 0 or n == 1:
        return 1
    fact = 1


    for i in range(2, n + 1):
        fact *= i

    return fact


num = 5
ans = factorial(num)
print(num)
