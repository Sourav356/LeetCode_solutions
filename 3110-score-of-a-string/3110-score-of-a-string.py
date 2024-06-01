class Solution:
    def scoreOfString(self, s: str) -> int:
        score = 0
    
    # Iterate through the string from the first character to the second to last character
        for i in range(len(s) - 1):
        # Calculate the absolute difference between ASCII values of adjacent characters
            diff = abs(ord(s[i]) - ord(s[i + 1]))
        # Add the difference to the score
            score += diff
    
        return score
        