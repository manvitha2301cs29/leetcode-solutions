from functools import lru_cache
class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums = [1] + nums + [1]
        n = len(nums)
        @lru_cache(None)
        def dp(i,j):
            
            maxi = 0 
            if i > j :
                return 0 
            
            for k in range(i,j+1):
                c = nums[i-1]*nums[k]*nums[j+ 1] + dp(i,k-1) + dp(k+1,j)
                maxi = max(c,maxi)
            return maxi 
        return dp(1,n-2)
            