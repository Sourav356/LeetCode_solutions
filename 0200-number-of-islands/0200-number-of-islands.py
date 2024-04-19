from collections import deque
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        rows, cols = len(grid), len(grid[0])
        visited_array = [[False] * cols for _ in range(rows)]
        directions = [(1,0),(-1,0),(0,1),(0,-1)]
        count= 0
        
        
        def bfs(i,j):
            queue = deque([(i,j)])
            visited_array[i][j] = True
            
            while queue:
                x,y = queue.popleft()
                for dx,dy in directions:
                    nx,ny = x+dx, y+dy
                    if 0<=nx < rows and 0<=ny<cols and not visited_array[nx][ny] and grid[nx][ny] == '1':
                        visited_array[nx][ny] = True
                        queue.append((nx,ny))
                
        for i in range(rows):
            for j in range(cols):
                if not visited_array[i][j] and grid[i][j] == '1':
                    count+=1
                    bfs(i,j)
                    
                    
        return count
        