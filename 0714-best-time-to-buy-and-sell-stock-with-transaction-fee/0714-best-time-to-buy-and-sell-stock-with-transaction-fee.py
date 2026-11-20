class Solution:
    def maxProfit(self, prices: list[int], fee: int) -> int:
        n = len(prices)
        """@lru_cache(maxsize = None)
        def help(i,buy):
            if i == n :
                return 0 
            if buy :
                return max(help(i+1,buy),help(i+1,buy-1) - prices[i])
            else :
                return max(help(i+1,buy),help(i+1,buy+1) + prices[i] - fee)
        return help(0,1)
        """
        hold = -prices[0]
        sell = 0 
        for i in range(1,n):
            prev_sell = sell
            hold = max(hold,prev_sell - prices[i])
            sell = max(sell,hold + prices[i] - fee )
        return sell
