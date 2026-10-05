class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        n = len(nums)
        k = k%n
        def rever(i,j):
            while i <= j :
                nums[i] , nums[j] = nums[j] , nums[i]
                i += 1 
                j -= 1 
        rever(0,n-1-k)
        rever(n-k,n-1)
        rever(0,n-1)