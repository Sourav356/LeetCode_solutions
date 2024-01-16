class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        sq_nums = []
        for i in range(len(nums)):
            sq =(nums[i])**2
            sq_nums.append(sq)
            i += 1
    
        sq_nums.sort()
        return sq_nums
        