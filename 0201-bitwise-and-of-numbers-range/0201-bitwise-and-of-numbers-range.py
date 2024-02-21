class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        if left == right:
            return left
        if right > 2**31 - 1:
            return 0
        shift= 0
        while left != right:
            left >>=1
            right >>=1
            shift +=1
        
        return left << shift