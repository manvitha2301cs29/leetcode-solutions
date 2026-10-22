class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m = len(matrix)
        n = len(matrix[0])
        res = []
        l = 0 
        r = n - 1 
        t = 0 
        b = m - 1 
        while l <= r and t <= b :
            for i in range(l,r+1):
                res.append(matrix[t][i])
            t += 1 
            for j in range(t,b+1):
                res.append(matrix[j][r])
            r -= 1
            if b >= t :
                for i in range(r,l-1 , -1):
                    res.append(matrix[b][i])
                b -= 1 
            if r >= l :
                for i in range(b , t-1 , -1):
                    res.append(matrix[i][l])
                l += 1 
        return res 