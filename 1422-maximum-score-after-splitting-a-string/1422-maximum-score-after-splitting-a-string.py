class Solution:
    def maxScore(self, s: str) -> int:
        n = len(s)
        maxScore = 0
        ZeroCount = 0
        Ones = s.count('1')
        
        for i in range(n - 1):
            if s[i] == '0':
                ZeroCount +=1
            else:
                Ones -=1
                
                
            maxScore =max(maxScore, ZeroCount + Ones)
            
        return maxScore
                
                
        