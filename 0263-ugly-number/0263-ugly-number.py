class Solution:
    def isUgly(self, n: int) -> bool:
        if n<=0:
            return False
        
        ugly_fe ={2,3,5}
        for factor in ugly_fe:
            while n%factor==0:
                n//=factor
        return n ==1
        
        