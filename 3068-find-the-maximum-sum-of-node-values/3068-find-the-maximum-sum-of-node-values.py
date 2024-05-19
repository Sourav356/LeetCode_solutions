class Solution:
    def maximumValueSum(self, nums: List[int], k: int, edges: List[List[int]]) -> int:
        n = len(nums)
        diff = [0] * n
        total_sum = sum(nums)
        
        for i in range(n):
            diff[i] = (nums[i] ^ k) - nums[i]
        
        diff.sort(reverse=True)
        
        for i in range(0, n, 2):
            if i + 1 == n:
                return total_sum
            pair_sum = diff[i] + diff[i + 1]
            if pair_sum > 0:
                total_sum += pair_sum
        
        return total_sum

        
        