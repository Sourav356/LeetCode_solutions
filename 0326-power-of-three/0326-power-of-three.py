class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        number = n
        if n == 0:
            return False
        new_divi = []
        while number%3 == 0:
            divi = number//3
            new_divi .append(divi)
            number = divi

        count = len(new_divi)
        if 3**count == n:
            return True
        else:
            return False
            
            
        