class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        n = len(nums)
        ans = []
        i = 0 
        nums.sort()
        for i in range(n-2):
            if i > 0 and nums[i] == nums[i-1] :
                continue 
            ha = nums[i] # one ele
            if ha > 0 :
                return ans 
            j = i + 1 
            k = n -1 
            while j < k :
                if nums[i] + nums[j] + nums[k] == 0 :
                    ans.append([nums[i],nums[j],nums[k]])
                    j += 1 
                    k -= 1
                    while j < k  and nums[j] == nums[j-1]:
                        j += 1 
                    while j < k and nums[k] == nums[k+1]:
                        k -= 1 
                elif nums[i] + nums[j] + nums[k] < 0 :
                    j += 1 
                else : 
                    k -= 1
        return ans 
                

