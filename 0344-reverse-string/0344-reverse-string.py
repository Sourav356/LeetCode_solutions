class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        #here the Tm_COm is O(n) and Sp_com is O(1)
        s.reverse()
        
        
        #or here the Tm_COm is O(n) and Sp_com is O(1)
        
        # left,right= 0, len(s) -1
        # while left < right:
        #     s[left],s[right]=s[right],s[left]
        #     left+=1
        #     right-=1
        
        
        #OR here the Tm_COm is O(n) and Sp_com is O(N) thats why this is not give the right output where but in other places it gives the right output
        # list_string =""
        # string_list=[]
        # for i in s:
        #     list_string+=i
        # reverse = list_string[::-1]
        # for char in reverse:
        #     string_list.append(char)
        # return string_list