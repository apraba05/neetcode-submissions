class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = 0
        sell = 0
        n = len(prices)
        maxProfit = 0

        for s in range(n):
            sell = s + 1
            while sell < n:
                profit = prices[sell] - prices[s]
                maxProfit = max(profit, maxProfit)
                sell += 1
        
        if (maxProfit < 0):
            return 0
        
        return maxProfit
            

        
