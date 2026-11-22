class Solution:
    def findNumberOfLIS(self, nums: list[int]) -> int:
        n = len(nums)
        dp = [1 for i in range(n)]

        maxi = -1 
        count = [1 for i in range(n)]

        for i in range(n):
            for j in range(i):
                if nums[i] > nums[j] :
                    if  dp[i] < 1 + dp[j]:
                        count[i] = count[j] 
                        dp[i] = 1 + dp[j]
                    elif dp[i] == 1 + dp[j]:
                        count[i] += count[j] 
                        dp[i] = 1 + dp[j]
                    
            maxi = max(maxi,dp[i])
        ans = 0 
        for i in range(n):
            if maxi == dp[i]:
                ans += count[i]
        return ans 