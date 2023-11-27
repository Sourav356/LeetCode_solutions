class Solution:

    def gcdOfStrings(self, str1: str, str2: str) -> str:
        def gcd_of_len(len1, len2):
            while len2:
                len1,len2 = len2, len1 % len2
            return len1
    
        len1 , len2 = len(str1) ,len(str2)
        
        gcd_len = gcd_of_len(len1,len2)
        
        common_divisor = str1[:gcd_len]
        
        if common_divisor *( len1 // gcd_len) == str1 and common_divisor *(len2 // gcd_len) == str2:
            return common_divisor
        else:
            return ""