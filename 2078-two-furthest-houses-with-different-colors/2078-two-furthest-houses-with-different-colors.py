class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        max_dis = 0
        n = len(colors)
        
        for i in range(n):
            for j in range(i+1,n):
                if colors[i] != colors[j]:
                    max_dis = max(max_dis, j - i)
                    
        return max_dis
            
        
        