from collections import deque
class Solution:
    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:
        n = len(grid)
        INF = float('inf')
    
    # Initialize the distance matrix with INF
        dist = [[INF] * n for _ in range(n)]
    
    # Queue for multi-source BFS
        queue = deque()
    
    # Initialize the queue with positions of all thieves
        for r in range(n):
            for c in range(n):
                if grid[r][c] == 1:
                    queue.append((r, c))
                    dist[r][c] = 0
    
    # Directions for moving in the grid
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    # Perform multi-source BFS to calculate minimum distance to any thief
        while queue:
            r, c = queue.popleft()
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < n and 0 <= nc < n and dist[nr][nc] == INF:
                    dist[nr][nc] = dist[r][c] + 1
                    queue.append((nr, nc))
    
    # Binary search on the safeness factor
        def canReachEndWithSafenessFactor(safeness_factor):
            if dist[0][0] < safeness_factor:
                return False
            queue = deque([(0, 0)])
            visited = [[False] * n for _ in range(n)]
            visited[0][0] = True
        
            while queue:
                r, c = queue.popleft()
                if (r, c) == (n-1, n-1):
                    return True
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < n and 0 <= nc < n and not visited[nr][nc] and dist[nr][nc] >= safeness_factor: 
                        visited[nr][nc] = True
                        queue.append((nr, nc))
            return False
    
        low, high = 0, min(dist[0][0], dist[n-1][n-1])
        while low < high:
            mid = (low + high + 1) // 2
            if canReachEndWithSafenessFactor(mid):
                low = mid
            else:
                high = mid - 1
    
        return low
        