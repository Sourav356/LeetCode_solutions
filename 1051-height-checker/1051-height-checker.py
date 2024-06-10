class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        hsort = heights.copy()
        heights.sort()
        count = 0
        for i in range(len(hsort)):
            if hsort[i] != heights[i]:
                count+=1
        return count

        