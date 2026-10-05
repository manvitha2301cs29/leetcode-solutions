class Solution:
    def getRow(self, rowIndex: int) -> list[int]:
        n = rowIndex 
        if n == 0 :
            return [1]
        if n ==1 :
            return [1,1]
        prev = [1,1]
        res = [1]
        for j in range(2,n+1):
            for i in range(1,len(prev)):
                haha = prev[i-1] + prev[i]
                res.append(haha)
            res.append(1)
            prev = res 
            res = [1]
        return prev 

