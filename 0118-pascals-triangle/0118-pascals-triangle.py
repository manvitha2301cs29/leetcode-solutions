class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        n = numRows
        res = [[1 for i in range(1,j+2)] for j in range(n)]
        for j in range(2,n):
            for i in range(1,j):
                res[j][i] = res[j-1][i-1] + res[j-1][i]
        return res 
