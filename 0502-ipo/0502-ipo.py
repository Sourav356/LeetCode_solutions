class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        min_heap = []
        # Max-heap for projects sorted by profit (use negative profit for max-heap)
        max_heap = []
        
        # Push all projects into the min-heap
        for i in range(len(profits)):
            heapq.heappush(min_heap, (capital[i], profits[i]))
        
        current_capital = w
        
        for _ in range(k):
            # Move all feasible projects from min-heap to max-heap
            while min_heap and min_heap[0][0] <= current_capital:
                cap, prof = heapq.heappop(min_heap)
                heapq.heappush(max_heap, -prof)
            
            # If no projects are feasible, break
            if not max_heap:
                break
            
            # Select the most profitable feasible project
            current_capital += -heapq.heappop(max_heap)
        
        return current_capital
        