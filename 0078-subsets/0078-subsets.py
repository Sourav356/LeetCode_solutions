from typing import List
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        
        def backtrack(start, current_subset):
            # Append a copy of current_subset to the result
            result.append(current_subset[:])
            
            for i in range(start, len(nums)):
                # Include nums[i] in the current subset
                current_subset.append(nums[i])
                # Move on to the next element
                backtrack(i + 1, current_subset)
                # Backtrack by removing nums[i] from the current subset
                current_subset.pop()
        
        backtrack(0, [])
        return result
        