class Solution:
    def pivotInteger(self, n: int) -> int:
        for i in range(1, n+1):
            left_sum = sum(range(1, i+1))
            right_sum = sum(range(i, n +1))
            
            if left_sum == right_sum:
                return i
                
        return -1
            
        
        