class Solution:
    def customSortString(self, order: str, s: str) -> str:
        char_count = {}
        for char in s:
            char_count[char] = char_count.get(char, 0) + 1
        
        result = ""
        for char in order:
            if char in char_count:
                result += char * char_count[char]
                
                del char_count[char]
                
        for char,count in char_count.items():
            result += char * count
            
        return result
                
        
    
        