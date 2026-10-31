class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res = []
        nums.sort()
        def solve(idx,path):
            
            res.append(path.copy())
            for i in range(idx,n):
                if i != idx and nums[i] == nums[i-1] :
                    continue
                path.append(nums[i]) 
                solve(i+1 ,path)
                path.pop()
        solve(0,[])
        return res 
                