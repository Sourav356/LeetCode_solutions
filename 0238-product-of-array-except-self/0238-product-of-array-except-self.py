class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result= [1]*n
        left_pro = 1
        
        for i in range(1, n):
            left_pro *=nums[i -1]
            result[i] *= left_pro
            
        right_pro = 1
        
        for i in range(n-2, -1, -1):
            right_pro *=nums[i + 1]
            result[i] *=right_pro
            
        return result