import math
class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        if num <= 1:
            return False
        else:
            divisor_sum  = 1
        
            for i in range(2, int(math.sqrt(num)) + 1):
                if num % i == 0:
                    divisor_sum += i
                    if i != num // i:  # Avoid counting the same divisor twice for perfect squares
                        divisor_sum += num // i

        if divisor_sum == num:
            return True 
        else:
            return False