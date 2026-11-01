class Solution:
    def partition(self, s: str) -> list[list[str]]:
        n = len(s)
        ans = []
        #state idx , path
        def palin(i,j):
            while i < j :
                if s[i] != s[j]:
                    return False 
                i += 1 
                j -=  1
            return True 
        def solve(idx,path):
            if idx == n :
                ans.append(path.copy())
                return 
            for i in range(idx,n):
                if palin(idx,i):
                    path.append(s[idx:i+1])
                    solve(i+1,path)
                    path.pop()
        solve(0,[])
        return ans 
