class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], indexDiff: int, valueDiff: int) -> bool:
        if indexDiff <= 0 or valueDiff < 0:
            return False
        buckets = {}
        for i, num in enumerate (nums):
            bucket_index = num // (valueDiff + 1)
            
            for j in range(bucket_index - 1, bucket_index + 2):
                if j in buckets and abs(buckets[j] - num) <= valueDiff:
                    return True
            
            buckets[bucket_index] = num
        
            if i >= indexDiff:
                del buckets[nums[i - indexDiff] // (valueDiff + 1)]
        
        return False
            
        
            
                    