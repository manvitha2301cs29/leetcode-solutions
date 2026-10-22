class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        n = len(numbers)
        i = 0 
        j = n -1 
        ans = []
        while i < j :
            haha = numbers[i] + numbers[j]
            if haha < target :
                i += 1 
            elif haha > target :
                j -=1 
            else :
                return [i+1,j+1]
        return [-1,-1]