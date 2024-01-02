class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        expeacted_sum = n * (n+1) //2
        actual_sum = sum(nums)
        missing_number = expeacted_sum - actual_sum
        return missing_number