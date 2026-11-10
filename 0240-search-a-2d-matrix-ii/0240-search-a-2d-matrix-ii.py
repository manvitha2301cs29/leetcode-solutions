class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        i = 0 
        j = n -1 
        while i < m and j >= 0 :
            ele = matrix[i][j]
            if ele > target :
                j -= 1 
            elif ele == target :
                return True 
            else :
                i += 1 
        return False 