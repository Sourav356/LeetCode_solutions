class Solution:
    def wonderfulSubstrings(self, word: str) -> int:
        count = [0] * 1024
        count[0] = 1  # For an empty string, it's considered wonderful.
        result = 0
        mask = 0
        for char in word:
            # Toggle the bit corresponding to the current character.
            mask ^= 1 << (ord(char) - ord('a'))
            result += count[mask]
            # Check all possible masks by toggling one bit at a time.
            for i in range(10):
                result += count[mask ^ (1 << i)]
            # Update the count for the current mask.
            count[mask] += 1
        return result