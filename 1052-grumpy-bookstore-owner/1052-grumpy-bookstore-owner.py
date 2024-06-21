class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        n = len(customers)
        
        # Calculate the number of customers that are satisfied without using the secret technique
        always_satisfied = 0
        for i in range(n):
            if grumpy[i] == 0:
                always_satisfied += customers[i]
        
        # Calculate the number of potentially satisfied customers if we use the secret technique
        additional_satisfied = 0
        max_additional_satisfied = 0
        
        # Initialize the first window
        for i in range(minutes):
            if i < n and grumpy[i] == 1:
                additional_satisfied += customers[i]
        max_additional_satisfied = additional_satisfied
        
        # Slide the window across the entire array
        for i in range(minutes, n):
            if grumpy[i] == 1:
                additional_satisfied += customers[i]
            if grumpy[i - minutes] == 1:
                additional_satisfied -= customers[i - minutes]
            max_additional_satisfied = max(max_additional_satisfied, additional_satisfied)
        
        # The result is the sum of the always satisfied customers and the maximum additional customers we can satisfy
        return always_satisfied + max_additional_satisfied
        
        