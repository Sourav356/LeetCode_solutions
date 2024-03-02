class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        count = 0
        nums.sort()

        if len(nums) < 2:
            return 0
    
    
        else:
            for i in range(len(nums)-1):
                sum_e = nums[i + 1] - nums[i]
                if sum_e > count:
                    count = sum_e
                    
        return count


        