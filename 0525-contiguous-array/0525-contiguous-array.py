class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        max_length = 0
        sum_indices_map = {0: -1}  # Initialize with a sum of 0 at index -1
        count = 0

        for i, num in enumerate(nums):
            if num == 0:
                count -= 1
            else:
                count += 1

        # Check if the current sum has been seen before
            if count in sum_indices_map:
                max_length = max(max_length, i - sum_indices_map[count])
            else:
                sum_indices_map[count] = i

        return max_length
        