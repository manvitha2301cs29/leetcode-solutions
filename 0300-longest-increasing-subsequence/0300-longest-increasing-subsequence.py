class Solution:
    def lengthOfLIS(self, nums: list[int]) -> int:
        n = len(nums)
        nex = [0]*(n+1)
        for i in range(n-1,-1,-1):
            curr = [0]*(n+1)
            for j in range(i-1,-2,-1):
                nt = nex[j+1]
                t = 0 
                if j == -1 or  nums[i] > nums[j]:
                    t = nex[i+1] + 1 
                curr[j+1] = max(t,nt)
            nex = curr 
        return nex[0]
