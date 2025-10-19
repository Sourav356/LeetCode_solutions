class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 :
            return False
       
        num = x
        rev_num = 0
        while x > 0:
            rem = x % 10
            rev_num = rev_num*10 + rem
            divi = x // 10
            x = divi

        return rev_num == num


        