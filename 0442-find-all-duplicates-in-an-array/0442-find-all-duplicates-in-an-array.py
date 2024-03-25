class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        dub = []
        n = len(nums)
        
        for num in nums:
            index = abs(num) - 1
            if nums[index] < 0:
                dub.append(abs(num))
            else:
                nums[index] = -nums[index]
        return dub