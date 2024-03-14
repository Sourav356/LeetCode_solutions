class Solution:
    def reverseVowels(self, s: str) -> str:
        list_v = [ 'a', 'e', 'i', 'o', 'u','A', 'E', 'I', 'O', 'U']
        left = 0
        right =len(s) - 1

        while left < right:
            if s[left] in list_v and s[right] in list_v:
                s = s[:left] + s[right] + s[left+1:right] + s[left] + s[right+1:]
                right -=1
                left+=1
            elif s[left] in list_v:
                right -= 1
            elif s[right] in list_v:
                left += 1
            else:
                left+=1
                right-1
                
        return s