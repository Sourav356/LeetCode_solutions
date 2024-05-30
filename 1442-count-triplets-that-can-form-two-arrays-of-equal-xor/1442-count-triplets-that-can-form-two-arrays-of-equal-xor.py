class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        from collections import defaultdict
    
        prefix = [0] * (len(arr) + 1)
        for i in range(len(arr)):
            prefix[i+1] = prefix[i] ^ arr[i]
    
        count = defaultdict(int)
        total = defaultdict(int)
        result = 0
    
        for k in range(len(arr)):
            if prefix[k+1] in count:
                result += count[prefix[k+1]] * k - total[prefix[k+1]]
            count[prefix[k]] += 1
            total[prefix[k]] += k
    
        return result
        