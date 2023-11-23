class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        start = 0
        end = 1
        k = 0
        while end < len(nums):
            if nums[start] != nums[end]:
                end+=1
                start+=1
            else:
                nums.pop(end)


        k=len(nums)
        print(k,",", nums + ['_']*(len(nums)-k))
