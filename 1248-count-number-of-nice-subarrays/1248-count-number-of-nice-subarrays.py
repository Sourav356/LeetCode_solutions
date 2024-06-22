class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        odd_count = 0
        count = 0
        prefix_counts = {0: 1}
        
        for num in nums:
            if num % 2 != 0:
                odd_count += 1
            
            if odd_count - k in prefix_counts:
                count += prefix_counts[odd_count - k]
            
            if odd_count in prefix_counts:
                prefix_counts[odd_count] += 1
            else:
                prefix_counts[odd_count] = 1
        
        return count
        