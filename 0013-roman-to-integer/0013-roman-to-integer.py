class Solution:
    def romanToInt(self, s: str) -> int:
        roman = {
            "I":1,"V": 5, "X":10,"L":50, "C":100, "D":500, "M":1000
        }

        Integer_value = 0
        Prev_value = 0
        for char in s[::-1]:
            value = roman[char]
            if value < Prev_value:
                Integer_value -= value
            else:
                Integer_value+= value
            Prev_value = value
        return Integer_value

 
            