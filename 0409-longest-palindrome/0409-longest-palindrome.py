class Solution:
    def longestPalindrome(self, s: str) -> int:
        freq_counter = {}
    
    # Count the frequency of each character
        for char in s:
            freq_counter[char] = freq_counter.get(char, 0) + 1
    
    # Initialize variables to keep track of the length of the longest palindrome
        length = 0
        has_odd_freq = False
    
    # Calculate the length of the longest palindrome
        for count in freq_counter.values():
            if count % 2 == 0:
                length += count
            else:
                length += count - 1
                has_odd_freq = True
    
    # Add 1 if there was at least one character with an odd frequency
        if has_odd_freq:
            length += 1
    
        return length
        