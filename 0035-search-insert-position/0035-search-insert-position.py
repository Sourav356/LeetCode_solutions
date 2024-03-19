class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left= 0
        if target not in nums:
            nums.append(target)
            new = nums.sort()
            for i in range(len(nums)):
                if nums[left] == target:
                    return left
                else:
                    left+=1
        
                i+=1
        else:
            for i in range(len(nums)):
                if nums[left] == target:
                    
                    return left
                else:
                    left+=1
        
            i+=1
        