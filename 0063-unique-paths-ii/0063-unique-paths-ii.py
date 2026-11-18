class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        if obstacleGrid[0][0] == 1 or obstacleGrid[m-1][n-1] == 1:
            return 0
        
        dp = [0]*n
        dp[0] = 1
        
        for i in range(m):
            # If current row start is blocked, reset to 0
            if obstacleGrid[i][0] == 1:
                dp[0] = 0
            
            for j in range(1, n):
                if obstacleGrid[i][j] == 1:
                    dp[j] = 0  # Can't reach this cell
                else:
                    dp[j] += dp[j-1]
        
        return dp[-1]