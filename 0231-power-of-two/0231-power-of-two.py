class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        return n >0 and (n & (n - 1)) == 0
    
    
    # or You can import math 
    # Then run 
    # return n > 0 and math.log2(n).is_integer()
        