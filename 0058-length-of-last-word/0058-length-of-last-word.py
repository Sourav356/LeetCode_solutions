class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        word = ""
        count = 0
        for char in reversed(s):
            if char!=" ":
                word =char + word
                count+=1
            elif count > 0:
                break 
        return count
        