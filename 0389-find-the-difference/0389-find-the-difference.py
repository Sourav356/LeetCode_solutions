from collections import Counter
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        s_count = Counter(s)
        t_count = Counter(t)
        
        diff_count = t_count - s_count
        
        for char,count in diff_count.items():
            if count == 1:
                return char