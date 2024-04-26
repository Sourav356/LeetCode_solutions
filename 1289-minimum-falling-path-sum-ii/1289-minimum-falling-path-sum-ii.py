class Solution:
    def minFallingPathSum(self, grid: List[List[int]]) -> int:
        
        n = len(grid)
        
        # Initialize dp array to store minimum sum for each cell
        
        dp = [[0] * n for _ in range(n)]
        
        # Copy the first row from the grid to the dp array
        dp[0] = grid[0]
        
        # Iterate over each row starting from the second row
        for i in range(1, n):
            for j in range(n):
                # Calculate the minimum sum for the current cell
                min_sum = float('inf')
                for k in range(n):
                    if k != j:
                        min_sum = min(min_sum, dp[i - 1][k])
                dp[i][j] = grid[i][j] + min_sum
        
        # Find the minimum sum from the last row
        return min(dp[-1])
        