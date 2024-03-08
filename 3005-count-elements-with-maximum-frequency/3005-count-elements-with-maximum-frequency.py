from collections import Counter
class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        fr_count = Counter(nums)
        max_fr = max(fr_count.values())
        
        total_ele = sum(1 for freq in fr_count.values() if freq == max_fr)
        total_fr = total_ele * max_fr
        return total_fr
        