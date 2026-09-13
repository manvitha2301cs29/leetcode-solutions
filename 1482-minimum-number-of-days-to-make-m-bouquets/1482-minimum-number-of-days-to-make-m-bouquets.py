class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        ans = - 1 
        low = min(bloomDay) 
        high = max(bloomDay)
        n = len(bloomDay)
        if m*k > n :
            return -1 
        def possible(mid):
            count = 0 
            flowers = 0 

            for day in bloomDay:
                if day <= mid :
                    flowers+= 1 
                    if flowers == k :
                        count += 1  
                        flowers = 0 
                else :
                    flowers = 0 


            
            return count >= m 
        while low <=high :
            mid = low + (high-low)//2 
            if possible(mid) :
                ans =  mid
                high = mid -1  
            else :
                low = mid + 1 
            
        return ans 

        


            

