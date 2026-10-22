class Solution:
    def summaryRanges(self, nums: list[int]) -> list[str]:
        n = len(nums)
        ans = []
        start = 0
        for i in range(1,n+1):
            if i == n or nums[i] != nums[i-1] + 1 :
                if start == i-1:
                    ans.append(f"{nums[start]}")
                else :
                    ans.append(f"{nums[start]}->{nums[i-1]}")
                start = i 
        return ans 

