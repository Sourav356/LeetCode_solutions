class Solution:
    def reverse(self, x: int) -> int:
        Max_int = 2**31 - 1
        Min_int = - 2**31

        actual = x
        rev_num = 0
        if x < 0:
            x = x * (-1)
        while x > 0:
            digit = x % 10
            rev_num = rev_num *10 + digit
            x = x // 10
        if rev_num > Max_int or rev_num < Min_int:
            return 0
        elif actual < 0 :
            rev_num_nege = rev_num * (-1)
            return rev_num_nege
        else:
            return rev_num
        