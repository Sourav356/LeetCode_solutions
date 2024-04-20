class Solution:
    def findFarmland(self, land: List[List[int]]) -> List[List[int]]:
        def dfs(r, c):
            nonlocal bottom_right
            for dr, dc in [(1, 0), (0, 1)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n and land[nr][nc] == 1 and not visited[nr][nc]:
                    visited[nr][nc] = True
                    bottom_right = (max(bottom_right[0], nr), max(bottom_right[1], nc))
                    dfs(nr, nc)

        m, n = len(land), len(land[0])
        visited = [[False] * n for _ in range(m)]
        result = []

        for i in range(m):
            for j in range(n):
                if land[i][j] == 1 and not visited[i][j]:
                    visited[i][j] = True
                    bottom_right = (i, j)
                    dfs(i, j)
                    result.append([i, j, bottom_right[0], bottom_right[1]])

        return result