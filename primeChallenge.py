# This program solves various problems related to
# prime numbers.

#---------------------------------------------
def isNumberPrime(n):
    isPrime = True
    endTestValue = number//2+1
    for testNumber in range(2, endTestValue):
        if number % testNumber == 0:
            isPrime = False
    return isPrime
#---------------------------------------------

# Count prime numbers between 2000 and 3000

count  = 0      # Will increment when a prime is detected
for number in range(2000,3001):
    if isNumberPrime(number):
        count = count + 1

print("Primes between 2000 and 3000:", count)

#---------------------------------------------

# Determine sum of prime numbers between 400 and 500

sum = 0   # Accumulator for sum
for number in range(400,501):
    if isNumberPrime(number):
        sum += number

print("Sum of primes between 400 and 500:", sum)

#---------------------------------------------

# Find first prime number over 1 million

number = 1000001
while ( not isNumberPrime(number) ):
    number = number + 1

print("First prime number over 1 million:", number)

#---------------------------------------------