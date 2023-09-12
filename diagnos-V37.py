# This might be a small code but I felt like adding a class to this anyway

# What this class does is keep track of our found prime numbers and a flag for if a nummber should be added to the list
# "PrimeNumbers" is the list that will keep track of our prime numbers
# "isPrime" is the flag that will let the code know if we can add the nummer to the list
class PrimeInfo():
    def __init__(self, primeNumbers = [], isPrime = False):
        self._primeNumbers = primeNumbers
        self._isPrime = isPrime
    
    def get_primeNumbers(self):
        return self._primeNumbers
    
    def set_primeNumbers(self, x):
        self._primeNumbers.append(x)

    def get_isPrime(self):
        return self._isPrime

    def set_isPrime(self, x):
        self._isPrime = x

primeInfo = PrimeInfo()

# Function to handle the prime numbers
def prime(n):

    # Range that goes from 2 to n
    for num in range(2,n+1):
        primeInfo.set_isPrime(True)

        # Check the previously found prime numbers to find out if "num" is also a prime number
        for primeNum in primeInfo.get_primeNumbers():
            if num % primeNum == 0:
                primeInfo.set_isPrime(False)
                break
        
        # If we find that "num" is a prime number we add it to the list
        if primeInfo.get_isPrime():
            primeInfo.set_primeNumbers(num)

    print('\n'.join(map(str, primeInfo.get_primeNumbers())))


prime(int(input('n: ')))