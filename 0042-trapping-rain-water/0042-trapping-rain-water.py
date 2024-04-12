class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        water = 0
        left, right = [0]*n, [0]*n
        left[0] = height[0]
        right[n-1] = height[n-1]
        
        for i in range(n):
            left[i] = max(left[i-1],height[i])
        for i in range(n-2,-1,-1):
            right[i] = max(right[i+1],height[i])
        
        for i in range(n):
            water+= min(left[i],right[i]) - height[i]

        return water
        
        