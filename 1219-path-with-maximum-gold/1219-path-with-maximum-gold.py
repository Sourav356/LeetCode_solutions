class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        dx = [-1, 0, 0, 1]
        dy = [0, -1, 1, 0]
        
        def dfs(i, j, grid):
            n = len(grid)
            m = len(grid[0])
            
            if i < 0 or i >= n or j < 0 or j >= m or grid[i][j] == 0:
                return 0
            
            curval = grid[i][j]
            grid[i][j] = 0  # Mark the cell as visited
            maxsum = 0
            
            for k in range(4):
                ni = i + dx[k]
                nj = j + dy[k]
                maxsum = max(maxsum, dfs(ni, nj, grid))
            
            grid[i][j] = curval  # Restore the cell's value
            
            return curval + maxsum
        
        n = len(grid)
        m = len(grid[0])
        ans = 0
        
        for i in range(n):
            for j in range(m):
                if grid[i][j] != 0:
                    ans = max(ans, dfs(i, j, grid))
                    
        return ans
        
                    
        
            
             
                
        