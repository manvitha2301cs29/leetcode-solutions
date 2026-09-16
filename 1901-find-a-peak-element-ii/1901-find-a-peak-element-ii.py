class Solution:
    def findPeakGrid(self, mat: List[List[int]]) -> List[int]:
        m = len(mat)
        n = len(mat[0])
        l = 0 
        h = n - 1 
        while l <= h :
            mi = l + (h-l)//2
            maxir = 0 
            for j in range(1,m):
                if mat[j][mi] > mat[maxir][mi]:
                    maxir = j 
            maxiel = mat[maxir][mi]
            le = mat[maxir][mi-1] if mi >= 1 else -1 
            re =  mat[maxir][mi+1] if mi < n - 1  else -1 
            if maxiel > re and maxiel > le :
                return [maxir , mi ]
            elif le > maxiel :
                h = mi - 1 
            else :
                l = mi + 1 
        return [0,0]