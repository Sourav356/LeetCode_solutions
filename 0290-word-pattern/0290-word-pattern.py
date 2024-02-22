class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split()

        if len(pattern) != len(words):
            return False
        p_map = {}
        s_map = {}

        for char , word in zip(pattern, words):
            if char in p_map and p_map[char] != word:
                return False 
            if word in s_map and s_map[word] != char:
                return False
                
            p_map[char] = word
            s_map[word] = char
            
        return True