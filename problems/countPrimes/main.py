class Solution:
    def countPrimes(self, n: int) -> int:

        count = 0

        for x in range(n):
            count += self.isPrime(x)

        return count
# this is exceeding the time limit rn
# lol it is slow
    def isPrime(self, n: int) -> bool:

        if n <= 1:
            return False
        if n <= 3:
            return True
        if n % 2 == 0 or n % 3 == 0:
            return False

        i = 5
        while i * i <= n:
            if n % i == 0 or n % (i + 2) == 0:
                return False
            i += 6

        return True


# not mine but I found this one and liked it
# I need to understand wtf is happening with this one
    def _countPrimes(self, n: int) -> int:

        is_prime = [0, 0] + [1] * (n - 2)
        
        for i in range(2, int(n ** 0.5) + 1):
            if is_prime[i] == 1:
                is_prime[i**2::i] = [0] * len(is_prime[i**2::i])

        return sum(is_prime)


# another good one I found
# mine kept timing out becuase my isPrime function is not super fast

def __countPrimes(self, n):

    if n < 3:
        return 0
    primes = [True] * n
    primes[0] = primes[1] = False

    for i in range(2, int(n ** 0.5) + 1):
        if primes[i]:
            primes[i * i: n: i] = [False] * len(primes[i * i: n: i])

    return sum(primes)