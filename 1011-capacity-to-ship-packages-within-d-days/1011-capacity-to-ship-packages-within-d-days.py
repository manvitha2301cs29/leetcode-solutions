class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        low = max(weights)
        high = sum(weights)
        n = len(weights)
        ans = high 

        def possible(mid):
            count = 1 
            day = 0 
            for w in weights :
                if w +day  > mid :
                    count += 1 
                    day = w 
                else :
                    day = day + w 
            return count <= days
        while low <= high :
            mid = low + (high-low)//2 
            if possible(mid) :
                high = mid -1 
                ans = mid 
            else :
                low = mid +1 
        return ans 
                    

                    

