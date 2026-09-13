class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        n = len(piles)
        low = 1 
        high = max(piles)
        def possible(x):
            sumi = 0 
            for i in piles :
                sumi += ceil(i/x)
            return sumi <= h 
        ans = -1 
        while low <= high :

            mid = low + (high - low)//2 
            if possible(mid) :
                ans = mid 
                high = mid - 1
                
            else :
                low = mid + 1 
        return ans 
