import math
def isPrime(a):
    for i in range(2, int(math.sqrt(a))):
        if(a%i==0):
            return False
    return True

sumA = 0
for i in range(2, 100):
    if(isPrime(i)):
            sumA += i

print(sumA)