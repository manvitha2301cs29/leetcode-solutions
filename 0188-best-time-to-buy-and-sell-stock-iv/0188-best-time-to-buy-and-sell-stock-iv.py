class Solution:
    def maxProfit(self, k: int, prices: list[int]) -> int:
        
        n = len(prices)

        def help(i,buy,nk,sumi):
            if i == n :
                return sumi 
            buyi = selli = -float('inf')
            if buy ==  0 :
                buyi = max(help(i+1,buy,nk,sumi) ,help(i+1,buy+1,nk,sumi - prices[i]))
            else :
                selli = max(help(i+1,buy,nk,sumi) ,help(i+1,buy-1,nk-1,sumi +prices[i]))
            return max(buyi ,selli)
        return help(0,0,k,0)
        

                 

