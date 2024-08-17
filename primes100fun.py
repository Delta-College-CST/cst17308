# This program determines the first 100 prime numbers

#---------------------------------------------
def isNumberPrime(n):
    isPrime = True
    endTestValue = number//2+1
    for testNumber in range(2, endTestValue):
        if number % testNumber == 0:
            isPrime = False
    return isPrime
#---------------------------------------------

PRIME_COUNT = 100

count  = 0      # Will increment when a prim is detected
number = 2      # Number to test for prime - start at 2

# Loop until 100 prime numbers are detected.  Variable
# 'number' is current candidate to be tested.  Variable
# 'count' keeps a running tally of prime numbers so far.
while count < PRIME_COUNT:

    # If prime, increment prime count and write number
    if isNumberPrime(number) == True:
        count = count + 1
        print(count,":",number)

    # Increment candidate number to test the next one
    number = number + 1
