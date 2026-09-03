class Solution:
    def minCost(self, n: int, cuts: List[int]) -> int:
        points = [0] + sorted(cuts) + [n]
        m = len(points)
        dp = [[float('inf') for i in range(m)] for i in range(m)]
        
        def solve(i,j):
            if j - i <= 1 :
                return 0 
            if dp[i][j] != float('inf'):
                return  dp[i][j]
            for k in range(i+1,j):
                dp[i][j] = min(dp[i][j] , solve(i,k) + solve(k,j) + points[j] - points[i]) 
            return dp[i][j]
        return solve(0,m-1)
