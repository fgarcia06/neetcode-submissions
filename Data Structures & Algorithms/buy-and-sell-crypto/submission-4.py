class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # 
        profit = 0

        for buy in range(len(prices)):
            for sell in range(len(prices)):
                if sell >= buy:
                    profit = max(profit, (prices[sell] - prices[buy]))

        return profit
        # Goal: return value of the maximum profit (int)