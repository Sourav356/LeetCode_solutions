class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        start = 0
        currentcost = 0
        maxlength = 0
        
        for end in range(len(s)):
            currentcost += abs(ord(s[end]) - ord(t[end]))
            
            while currentcost > maxCost:
                currentcost -= abs(ord(s[start]) - ord(t[start]))
                start +=1
                
            maxlength = max(maxlength, end - start + 1)
            
        return maxlength
        