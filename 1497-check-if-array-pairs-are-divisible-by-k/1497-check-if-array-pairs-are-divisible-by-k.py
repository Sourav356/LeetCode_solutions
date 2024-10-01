class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        remainder_count = [0] * k

    # Count remainders
        for num in arr:
            remainder = num % k
            if remainder < 0:
                remainder += k
            remainder_count[remainder] += 1

    # Check if the pairs can be formed
        for i in range(1, k):
            if i == k - i:  # Special case for when remainder is k/2
                if remainder_count[i] % 2 != 0:
                    return False
            elif remainder_count[i] != remainder_count[k - i]:
                return False

    # Check remainder 0
        if remainder_count[0] % 2 != 0:
            return False

        return True
        