from collections import Counter
class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        freq_count = Counter(arr)
    
    # Step 2: Sort the integers based on their frequencies
        sorted_freq = sorted(freq_count.values())
    
    # Step 3: Remove the smallest frequency integers until total removed elements >= k
        unique_count = len(sorted_freq)
        removed_count = 0
        for freq in sorted_freq:
            if removed_count + freq <= k:
                removed_count += freq
                unique_count -= 1
            else:
                break
    
    # Step 4: Return the count of unique integers remaining after removing k elements
        return unique_count