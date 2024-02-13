class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        for i in range(len(words)):
            Not_re = words[i]
            re= Not_re[::-1]
            if Not_re == re:
                return Not_re
            
        return ""
        
        
        