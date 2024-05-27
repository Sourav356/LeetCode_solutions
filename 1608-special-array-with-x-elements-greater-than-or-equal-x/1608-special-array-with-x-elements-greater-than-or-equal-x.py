class Solution:
    def specialArray(self, nums: List[int]) -> int:
        nums.sort(reverse=True)  # Sort the array in descending order
    
        for i in range(len(nums)):
            if i < nums[i] and (i == len(nums) - 1 or i + 1 > nums[i + 1]):
                return i + 1
    
        return -1
        