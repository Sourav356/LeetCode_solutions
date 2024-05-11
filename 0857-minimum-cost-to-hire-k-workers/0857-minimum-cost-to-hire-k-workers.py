import heapq
class Solution:
    def mincostToHireWorkers(self, quality: List[int], wage: List[int], k: int) -> float:
        n = len(quality)
        workers = sorted([(w / q, q) for w, q in zip(wage, quality)])
        
        total_quality = 0
        min_cost = float('inf')
        heap = []
        
        for ratio, q in workers:
            total_quality += q
            heapq.heappush(heap, -q)  # Min-heap with negative values for maximum value extraction
            
            if len(heap) > k:
                total_quality += heapq.heappop(heap)  # Remove the worker with the highest quality from the heap
            
            if len(heap) == k:
                min_cost = min(min_cost, total_quality * ratio)
        
        return min_cost
        