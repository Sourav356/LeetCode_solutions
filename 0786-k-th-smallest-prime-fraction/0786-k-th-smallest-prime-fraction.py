# from fractions import Fraction
import heapq
class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
#         This solution is good for small inputs
#         ratios = []
#         for i in range(len(arr) -1):
#             for j in range(i+1, len(arr)):
#                 ratios.append(Fraction(arr[i],arr[j]))    
#         ratios.sort()
#         if k == 1:
#             small = ratios[0]
#         else:
#             small = ratios[k - 1]
            
#         kth_small = [small.numerator , small.denominator]
        
#         return kth_small

# More optimize solution is using Heap
        n = len(arr)
        heap = [(arr[0]/arr[j], 0,j) for j in range(1 , n)]
        heapq.heapify(heap)
        
        for _ in range(k -1):
            _, i, j = heapq.heappop(heap)
            if i+1 < j:
                heapq.heappush(heap, (arr[i+1]/arr[j], i+1,j))
                
        _,i,j = heapq.heappop(heap)
        return [arr[i],arr[j]]

        