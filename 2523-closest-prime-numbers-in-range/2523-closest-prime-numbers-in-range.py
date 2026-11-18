class Solution:
    def closestPrimes(self, left: int, right: int) -> list[int]:

        def sieve(n):
            primes = []
            is_prime = [True] * (n + 1)
            is_prime[0] = is_prime[1] = False

            for p in range(2, int(n**0.5) + 1):
                if is_prime[p]:
                    for i in range(p * p, n + 1, p):
                        is_prime[i] = False

            for p in range(left, n + 1):
                if is_prime[p]:
                    primes.append(p)

            return primes

        primes = sieve(right)

        if len(primes) < 2:
            return [-1, -1]

        ans = [-1, -1]
        min_diff = float('inf')

        for i in range(len(primes) - 1):
            diff = primes[i + 1] - primes[i]

            if diff < min_diff:
                min_diff = diff
                ans = [primes[i], primes[i + 1]]

        return ans