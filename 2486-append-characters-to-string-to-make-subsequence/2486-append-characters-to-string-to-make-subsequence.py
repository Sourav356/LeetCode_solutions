class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        s_pointer, t_pointer = 0, 0
        s_len, t_len = len(s), len(t)
    
    # Traverse both strings to find the longest subsequence of t in s
        while s_pointer < s_len and t_pointer < t_len:
            if s[s_pointer] == t[t_pointer]:
                t_pointer += 1
            s_pointer += 1
    
    # The number of characters in t that were not found in s
        missing_characters = t_len - t_pointer
    
        return missing_characters
        
            
        