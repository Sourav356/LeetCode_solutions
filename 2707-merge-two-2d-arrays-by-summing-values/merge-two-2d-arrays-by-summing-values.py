class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        hashtable = {}

        for id, value in nums1:
            hashtable[id] = hashtable.get(id, 0) + value

        for id, value in nums2:
            hashtable[id] = hashtable.get(id,0) + value

        result = sorted([[id,val] for id, val in hashtable.items()])

        return result

        