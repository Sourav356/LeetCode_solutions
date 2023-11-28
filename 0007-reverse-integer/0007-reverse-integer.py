class Solution:
    def reverse(self, x: int) -> int:
        abs_x = abs(x)
        str_x = str(abs_x)
        str_X_X = str_x[::-1]
        str_to_int = int(str_X_X)
        if x < 0:
            str_to_int *= -1
        if -2147483648 <= str_to_int <= 2147483647:
            return (str_to_int)
        else:
            return 0
        