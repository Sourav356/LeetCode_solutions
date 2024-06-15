class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        freq = Counter(arr1)
        
        # Step 2: Initialize the result list
        result = []
        
        # Step 3: Add elements from arr2 in order
        for num in arr2:
            if num in freq:
                result.extend([num] * freq[num])
                del freq[num]
        
        # Step 4: Add the remaining elements not in arr2, sorted
        remaining = []
        for num in freq:
            remaining.extend([num] * freq[num])
        
        result.extend(sorted(remaining))
        
        return result
        