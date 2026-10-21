class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        sumi = 0 
        l = prices[0]
        n = len(prices)
        for i in range(1,n):
            if l < prices[i]:
                 
                sumi += prices[i] - l 
            l = prices[i] 
        return sumi 
