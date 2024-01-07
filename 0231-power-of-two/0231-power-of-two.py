class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        number = n
        if n == 0:
            return False
        new_divi = []
        while number%2 == 0:
            divi = number//2
            new_divi .append(divi)
            number = divi

        count = len(new_divi)
        print(count)
        if 2**count == n:
            return True
        else:
            return False
        
        
        
        
        
    
    # return n >0 and (n & (n - 1)) == 0
    # or You can import math 
    # Then run 
    # return n > 0 and math.log2(n).is_integer()
        