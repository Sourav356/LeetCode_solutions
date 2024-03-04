class Solution:
    def findNonMinOrMax(self, nums: List[int]) -> int:
        nums.sort()
        mini = nums[0]
        max_m = nums[len(nums) -1]

        for num in nums:
            if num > mini and num < max_m:
                return num
                break
        return -1
            
        