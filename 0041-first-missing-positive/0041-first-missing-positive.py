class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        i = 0
        while i < n:
        # Check if the current number is in the valid range and not in its correct position
            if 1 <= nums[i] <= n and nums[i] != nums[nums[i] - 1]:
            # Swap the current number with the number at its correct position
                nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]
            else:
                i += 1

                
                
        for i, num in enumerate(nums):
            if num != i + 1:
                return i + 1 
            
        return n + 1
        