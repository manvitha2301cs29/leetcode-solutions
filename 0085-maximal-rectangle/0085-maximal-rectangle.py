class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        r = len(matrix)
        c = len(matrix[0])
        maxi = 0 
        heights = [0]*(c+1)
        for i in range(r) :
            for j in range(c):
                heights[j] =  heights[j] + 1 if matrix[i][j] == "1" else 0
            stack = []
            for i , h in enumerate(heights):
                while  stack and h <= heights[stack[-1]]:
                    j = stack.pop()
                    ele = heights[j]
                    width = i if not stack else  i - stack[-1] - 1 
                    maxi = max(maxi , ele*(width))
                stack.append(i)
        return maxi 

            