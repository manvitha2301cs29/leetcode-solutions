class Solution:
    def lengthOfLIS(self, nums: list[int]) -> int:
        arr = nums
        n = len(arr)
        dp = [1 for i in range(n)]
        
        maxi = 0 
        start = -1 
        for i in range(n):
            for p in range(i):
                if arr[p] < arr[i] and 1 + dp[p] > dp[i]:
                    dp[i] = 1 + dp[p]
                    
            if maxi < dp[i]:
                maxi = dp[i]
                start = i
        return maxi 