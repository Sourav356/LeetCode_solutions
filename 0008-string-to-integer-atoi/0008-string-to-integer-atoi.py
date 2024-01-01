class Solution:
    def myAtoi(self, s: str) -> int:
        i = 0
        while i < len(s) and s[i].isspace():
            i += 1

        # Step 2: Check for '+' or '-'
        sign = 1
        if i < len(s) and (s[i] == '+' or s[i] == '-'):
            sign = -1 if s[i] == '-' else 1
            i += 1

        # Step 3: Read in digits until non-digit or end of input
        result = 0
        while i < len(s) and s[i].isdigit():
            digit = int(s[i])
            # Step 4: Convert digits into an integer
            result = result * 10 + digit
            i += 1
            
        result *= sign

        # Step 6: Clamp to the 32-bit signed integer range
        INT_MIN, INT_MAX = -2**31, 2**31 - 1
        if result < INT_MIN:
            return INT_MIN
        elif result > INT_MAX:
            return INT_MAX
        else:
            return result
        