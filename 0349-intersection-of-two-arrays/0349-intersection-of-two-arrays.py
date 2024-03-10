class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        nums2.sort()
        dic = []

        for i in range(len(nums1)):
            for j in range(len(nums2)):
                if  nums1[i] == nums2[j] and nums2[j]  not in dic:
                    dic.append(nums2[j])
                    
        return dic
        