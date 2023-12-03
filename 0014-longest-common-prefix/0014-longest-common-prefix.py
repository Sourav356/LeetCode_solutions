class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        prefix = strs[0]
        for string in strs[1:]:
            i = 0
            while i < len(prefix) and i <len(string) and prefix[i] == string[i]:
                i+=1
            prefix = prefix[:i]
                
                
            if not prefix:
                break 
        return prefix
        
        
        