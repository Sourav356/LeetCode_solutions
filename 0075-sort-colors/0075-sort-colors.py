class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def swap(nums, i , j):
            temp = nums[i]
            nums[i] = nums[j]
            nums[j] = temp
            
        for i in range(len(nums)):
            mini = i
            for j in range(i+1, len(nums)):
                if nums[j] < nums[mini]:
                    mini = j
            
            if mini != i:
               swap(nums, i , mini) 
        
        return nums