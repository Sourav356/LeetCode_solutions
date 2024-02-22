class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        s_map = {}
        t_map = {}
        
        for s_char , t_char in zip(s, t):
            if s_char in s_map and s_map[s_char] != t_char:
                return False
            if t_char in t_map and t_map[t_char]!= s_char:
                return False
            
            s_map[s_char] = t_char
            t_map[t_char] = s_char
            
            
        return True
            