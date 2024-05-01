class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        re_str = ''
        last_str=''
        if ch in word:
            for i, indices in enumerate (word):
                if word[i] == ch:
                    index = i
                    re_str+= indices
                    break 
                else:
                    re_str += indices
            reverse_str = re_str[::-1]
            for char in range(index+1,len(word)):
                last_str+=word[char]
    
            actually_str =reverse_str +last_str 
            return actually_str
        else:
            return word
    
        