class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        l = 0 

        for r in range(len(prices)): 
            curr_profit = prices[r] - prices[l]

            profit = max(profit, curr_profit)

            if prices[l] > prices[r]:
                l = r
        return profit
            

            