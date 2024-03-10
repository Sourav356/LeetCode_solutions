from collections import Counter
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        count = Counter(nums1)
        
        inters = []
        
        for num in nums2:
            if num in count and count[num] > 0:
                inters.append(num)
                
                count[num]-=1
        
        return inters
        
        
        