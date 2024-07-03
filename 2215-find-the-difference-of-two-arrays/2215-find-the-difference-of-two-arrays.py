class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
#         dn1 = []
#         dn2 = []
#         result = []
#         for i in range(len(nums1)):
#             if nums1[i] not in nums2:
#                 if nums1[i] not in dn1:
#                     dn1.append(nums1[i])
#         result.append(dn1)
#         for i in range(len(nums2)):
#             if nums2[i] not in nums1:
#                 if nums2[i] not in dn2:
#                     dn2.append(nums2[i])
#         result.append(dn2)
                
#         return result
        set2 = set(nums2)
        dn1 = set()
        dn2 = set()
        
        for num in nums1:
            if num not in set2:
                dn1.add(num)
        for num in nums2:
            if num not in set(nums1):
                dn2.add(num)
        
        return [list(dn1), list(dn2)]
                
                
                
        
                
        