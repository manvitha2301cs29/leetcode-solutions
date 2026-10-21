class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxi = 0 
        n = len(prices)
        mini = prices[0]
        for  i in range(1,n):
            if prices[i] < mini :
                mini = prices[i]
            else :
                maxi = max(maxi,prices[i] - mini)
        return maxi 