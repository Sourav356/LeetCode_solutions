class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        jobs = sorted(zip(difficulty, profit))
        # Sort the worker list
        worker.sort()

        max_profit = 0
        total_profit = 0
        j = 0

        # Iterate through each worker
        for ability in worker:
            # Update the max_profit for the current ability
            while j < len(jobs) and ability >= jobs[j][0]:
                max_profit = max(max_profit, jobs[j][1])
                j += 1
            # Add the max_profit that the current worker can get
            total_profit += max_profit
        
        return total_profit
        