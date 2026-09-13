class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        low = 1
        high = max(nums)
        n = len(nums)
        ans = high 

        #fffftttt
        def possible(x):
            sumi = 0 
            for i in nums :
                sumi += ceil(i/x)
            return sumi <= threshold
        
        while low <= high :
            mid = low + (high -low )//2 
            if possible(mid):
                ans = mid 
                high = mid -1 
            else :
                low = mid +1 
        return ans