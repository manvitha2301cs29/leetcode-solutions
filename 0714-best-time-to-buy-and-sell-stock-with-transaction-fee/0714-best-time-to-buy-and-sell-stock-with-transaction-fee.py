class Solution:
    def maxProfit(self, prices: list[int], fee: int) -> int:
        n = len(prices)
        @lru_cache(maxsize = None)
        def help(i,buy):
            if i == n :
                return 0 
            if buy :
                return max(help(i+1,buy),help(i+1,buy-1) - prices[i])
            else :
                return max(help(i+1,buy),help(i+1,buy+1) + prices[i] - fee)
        return help(0,1)
