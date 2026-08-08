class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        min_price = prices[0]

        for i in range(len(prices)): 

            if prices[i] < min_price:
                min_price = prices[i]

            else: # current price is greater than the min price (profit possible)
                profit = prices[i] - min_price
                if profit > max_profit:
                    max_profit = profit

        return max_profit