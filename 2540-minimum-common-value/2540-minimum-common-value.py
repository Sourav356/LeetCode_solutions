class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        i = 0
        j = 0
        common_min = float('inf')
        
        while i < len(nums1) and j < len(nums2):
            if nums1[i] == nums2[j]:
                common_min = min(common_min, nums1[i])
                i += 1
                j += 1
            elif nums1[i] < nums2[j]:
                i += 1
            else:
                j += 1
                
        if common_min != float('inf'):
            return common_min
        else:
            return -1
        