class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        n = len(prices)
        @lru_cache(maxsize = None)
        def help(i,canbuy,cool):
            if i == n :
                return 0 
            if not cool :
                if canbuy :
                    return max(help(i+1,canbuy,cool),help(i+1,canbuy-1 ,cool) - prices[i])
                else :
                    return max(help(i+1,canbuy,cool), help(i+1,canbuy+1,cool + 1) + prices[i])
            else :
                return help(i+1,canbuy,cool-1)
        return help(0,1,0)