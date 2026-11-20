class Solution:
    def maxProfit(self, k: int, prices: list[int]) -> int:
        
        n = len(prices)
        @lru_cache(maxsize = None)
        def help(i,buy,nk):
            if i == n or nk == 0  :
                return 0 
            
            if buy ==  0 :
                return  max(help(i+1,buy,nk) ,help(i+1,buy+1,nk) - prices[i])
            else :
                return max(help(i+1,buy,nk) ,help(i+1,buy-1,nk-1) +prices[i])
            
        return help(0,0,k)
        

                 

