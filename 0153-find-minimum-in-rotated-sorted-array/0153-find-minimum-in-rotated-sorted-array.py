class Solution:
    def findMin(self, nums: list[int]) -> int:
        n = len(nums)
        l = 0 
        h = n -1 
        while l < h :
            m = l + (h-l)//2 
            if nums[m] > nums[h] :
                l = m + 1 
            else :
                h = m 
        return nums[l] 
                