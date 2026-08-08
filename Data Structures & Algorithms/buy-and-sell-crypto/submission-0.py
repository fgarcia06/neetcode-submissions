class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # brute force solution
        max_profit = 0

        for i in range(len(prices)):
            buy_day = prices[i]

            for j in range(i+1, len(prices)):
                sell_day = prices[j]

                profit = sell_day - buy_day

                if profit > max_profit:
                    max_profit = profit
        
        return max_profit