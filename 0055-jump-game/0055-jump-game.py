class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        far = nums[0]
        for i in range(n):
            if i > far :
                return False 
            else :
                far = max(far , i + nums[i])

        return True 

            