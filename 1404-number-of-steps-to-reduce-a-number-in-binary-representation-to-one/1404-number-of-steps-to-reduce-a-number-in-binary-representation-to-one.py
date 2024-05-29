class Solution:
    def numSteps(self, s: str) -> int:
        decimal = int(s,2)
        count = 0
        while decimal > 1:
            if decimal % 2 == 0:
                decimal //= 2
                count+=1
            else:
                decimal+=1
                count+=1
                
        return count
        