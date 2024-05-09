class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        happiness.sort(reverse=True)  # Sort happiness array in descending order
        max_sum = 0
        for i in range(min(k, len(happiness))):  # Select up to k children or all children if k is larger than the array size
            max_sum += max(0, happiness[i] - i)  # Add the happiness value of the selected child, considering the decrement for unselected children
        return max_sum
                

        