class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        arr.sort()
        left = 0
        right = 1
        occurrences = []
        while left < len(arr):
            while right < len(arr) and arr[left] == arr[right]:
                right += 1
            
            occurrences.append(right - left)
            
            left = right
            right += 1
        
        unique_occurrences = len(occurrences) == len(set(occurrences))
        return unique_occurrences
        