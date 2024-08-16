# This program determines the first 100 prime nmbers

#---------------------------------------------
def isNumberPrime(number):
    isPrime = True
    endTestValue = number//2 + 1
    for testNumber in range(2, endTestValue):
        if number % testNumber == 0:
            isPrime = False
    return isPrime
#---------------------------------------------

aNumber = int(input())

if isNumberPrime(aNumber):
    print(aNumber,"is PRIME")
else:
    print(aNumber,"is NOT PRIME")
