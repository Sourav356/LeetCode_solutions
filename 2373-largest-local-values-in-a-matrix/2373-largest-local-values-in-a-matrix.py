class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        def getmax(grid, row, col):
            max_val = 0
            for i in range(row, row+3):
                for j in range(col, col+3):
                    max_val = max(grid[i][j], max_val)
            return max_val
        
        n = len(grid)
        ans = []
        for _ in range(n - 2):     #creating a 2D list length of (n - 2) using for loop
            ans.append([0]*(n-2))
            
        for i in range(len(ans)):
            for j in range(len(ans[0])):
                ans[i][j] = getmax(grid, i, j)
        return ans
    
        
        