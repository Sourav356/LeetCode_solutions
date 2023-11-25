class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        com_dict = {}
        
        for i,num in enumerate (nums):
            if num in com_dict:
                return [com_dict[num],i]
            else:
                complement = target - num
                com_dict[complement] = i
        return com_dict
        
        