class Solution:
    def tribonacci(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1 or n == 2:
            return 1
        
        # Initialize array to store Tribonacci sequence values
        tribonacci_values = [0] * (n + 1)
        tribonacci_values[1] = 1
        tribonacci_values[2] = 1
        
        # Compute Tribonacci sequence using dynamic programming
        for i in range(3, n + 1):
            tribonacci_values[i] = tribonacci_values[i - 1] + tribonacci_values[i - 2] + tribonacci_values[i - 3]
        
        return tribonacci_values[n]
        
        
                
    