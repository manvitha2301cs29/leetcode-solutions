class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        n = len(nums)
        if target > sum(nums):
            return 0 
        mini = float('inf') 
        i = 0 

        sumi = 0 
        for j in range(n):
            sumi += nums[j]
            while sumi >= target and i <= j :
                mini = min(mini , j-i+1)
                sumi -= nums[i]
                i += 1
        return mini 
