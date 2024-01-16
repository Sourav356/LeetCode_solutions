class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        index = 0
        for i in range(len(nums1)):
            if nums1[i] == 0 and index < len(nums2):
                nums1[i] = nums2[index]
                index+=1
        nums1.sort()
        