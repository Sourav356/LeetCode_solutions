class Solution:
    def matrixScore(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

    # Step 1: Toggle rows if the leftmost bit is 0
        for i in range(m):
            if grid[i][0] == 0:
                for j in range(n):
                    grid[i][j] ^= 1

    # Step 2: Toggle columns to maximize the number of 1s
        for j in range(1, n):
            count_ones = sum(grid[i][j] for i in range(m))
            if count_ones < m - count_ones:
                for i in range(m):
                    grid[i][j] ^= 1

    # Step 3: Calculate the score
        score = sum(int("".join(map(str, row)), 2) for row in grid)
        return score
        