class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        miss = 1
        added_patches = 0
        i = 0
    
        while miss <= n:
            if i < len(nums) and nums[i] <= miss:
                miss += nums[i]
                i += 1
            else:
                miss += miss
                added_patches += 1
    
        return added_patches
        