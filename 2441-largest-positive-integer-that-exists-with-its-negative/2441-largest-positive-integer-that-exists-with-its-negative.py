class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        neg = []
        pos = []
        arr = []
        for i in range(len(nums)):
            if nums[i] < 0:
                neg.append(nums[i])
            else:
                pos.append(nums[i])
        for i in range(len(neg)):
            if neg[i]*(-1) in pos:
                arr.append(neg[i]*(-1))
        
        if not arr:
            return -1
        else:
            max_arr = max(arr)
            return max_arr
