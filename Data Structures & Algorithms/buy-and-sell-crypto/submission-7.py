class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # 
        profit = 0
        min_price = prices[0]

        for i in range(len(prices)):

            if prices[i] < min_price:
                min_price = prices[i]
            
            curr_profit = prices[i] - min_price

            if curr_profit > profit:
                profit = curr_profit
        
        return profit