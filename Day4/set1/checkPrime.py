def checkPrime(num):
    count = 0

    for i in range(1, num + 1):
        if num % i == 0:
            count += 1

    if count == 2:
        return True
    else:
        return False


inNum=6
if(checkPrime(inNum)):
    print("Yes")
else:
    print("No")