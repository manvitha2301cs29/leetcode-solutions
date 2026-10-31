class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        n = len(candidates)
        res = []
        candidates.sort()
        def solve(idx,rem,path):
            if rem == 0 :
                res.append(path.copy())
                return 
            for i in range(idx,n):
                if i != idx and candidates[i] == candidates[i-1]:
                    continue 
                if candidates[i] > rem :
                    break 
                path.append(candidates[i])
                solve(i+1,rem -candidates[i],path)
                path.pop()

        solve(0,target ,[])
        return res 
        