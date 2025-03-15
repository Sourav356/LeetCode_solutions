class Solution:
    def minCapability(self, nums: List[int], k: int) -> int:
        left, right = min(nums), max(nums)

        def canRob(mid):
            count, i = 0, 0
            while i < len(nums):
                if nums[i] <= mid:  # Rob this house
                    count += 1
                    i += 1  # Skip the next house (no adjacent)
                i += 1  # Move to the next house
            return count >= k

        while left < right:
            mid = (left + right) // 2
            if canRob(mid):
                right = mid  # Try a smaller capability
            else:
                left = mid + 1  # Increase capability

        return left
        