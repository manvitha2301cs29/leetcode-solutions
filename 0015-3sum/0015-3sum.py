class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        n = len(nums)
        i = 0 
        nums.sort()
        res = []
        while  i < n-2:

            while i > 0 and i < n-2 and nums[i] == nums[i-1]:
                i += 1 
            j = i + 1 
            k = n - 1 
            while j < k :
                baby = nums[i] + nums[j] + nums[k]
                if baby == 0 :
                    res.append([nums[i],nums[j],nums[k]])
                    j+= 1 
                    k -= 1 
                    while j < k and nums[j] == nums[j-1]:

                        j += 1
                    while k > j and nums[k] == nums[k+1]:
                        k -= 1 
                elif baby < 0 :
                    j += 1 
                     
                    

                else :
                    k -= 1 
                
                
            i += 1 
        return res  
                