class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        count = {'a': 0, 'b': 0, 'c': 0}
        left = 0
        total = 0
        n = len(s)

        for right in range(n):
            count[s[right]] += 1

            while all(count[char] > 0 for char in "abc"):
                total += (n - right)  # Count all substrings ending at 'right'
                count[s[left]] -= 1  # Shrink the window from left
                left += 1

        return total
        