class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        n = len(candidates)
        candidates.sort()
        ans = []
        def solve(idx,rem , path):
            if rem == 0 :
                ans.append(path.copy())
                return 
            if idx == n :
                return 
            for i in range(idx,n):
                if candidates[i] > rem :
                    break 
                path.append(candidates[i])
                solve(i,rem-candidates[i],path)
                path.pop()
        solve(0,target,[])
        return ans 