class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        
        max_price =float('-inf')
        min_price = float('inf')
        profit = 0
        
        for price in prices:
            if price< min_price:
                min_price = price
            elif price - min_price  > profit:
                profit = price - min_price
                
        return profit
                