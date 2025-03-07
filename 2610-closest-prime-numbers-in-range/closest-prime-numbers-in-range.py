class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        def sieve(limit):
            is_prime = [True] * (limit + 1)
            is_prime[0] = is_prime[1] = False  # 0 and 1 are not prime

            for num in range(2, int(limit**0.5) + 1):
                if is_prime[num]:  # Mark multiples of num as non-prime
                    for multiple in range(num * num, limit + 1, num):
                        is_prime[multiple] = False
        
            return is_prime

    # Step 1: Compute primes up to `right` using Sieve of Eratosthenes
        is_prime = sieve(right)

    # Step 2: Collect all prime numbers in the range [left, right]
        primes = [num for num in range(left, right + 1) if is_prime[num]]

    # Step 3: Find the closest prime pair
        if len(primes) < 2:
            return [-1, -1]  # No valid pair exists

        min_diff = float('inf')
        ans = [-1, -1]

        for i in range(len(primes) - 1):
            diff = primes[i + 1] - primes[i]
            if diff < min_diff:
                min_diff = diff
                ans = [primes[i], primes[i + 1]]

        return ans

        