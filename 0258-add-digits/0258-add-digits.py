class Solution:
    def addDigits(self, num: int) -> int:
        nums_len = len(str(num))
        if nums_len > 1:
            for item in range(nums_len):
                mod = num %10
                divi = num//10
                add = mod + divi
                num = add
                
            return num

        else:
            return num
        