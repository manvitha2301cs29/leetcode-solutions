class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        cand = nums[0]
        count = 1 
        for i in range(1,n):
            if nums[i] == cand :
                count += 1 
            else :
                count -= 1 
                if count == 0 :
                    cand= nums[i]
                    count = 1 
        return cand 
