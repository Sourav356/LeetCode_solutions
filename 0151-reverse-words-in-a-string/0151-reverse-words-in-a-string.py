class Solution:
    def reverseWords(self, s: str) -> str:
        word_list = s.split()
        left, right = 0 , len(word_list) -1
        
        while left < right:
            word_list[left], word_list[right] = word_list[right] , word_list[left]
            
            left +=1
            right -=1
            
        sen = " ".join(word_list)
        
        return sen
        