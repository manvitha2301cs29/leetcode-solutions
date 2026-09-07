class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        n = len(stones)
        # indirectly asking no of groups formed 
        # we can form a group if it has same x or  y 
        # ans = n - no of groups 
        # we can find no of connected components with dfs 
        vis = set()
        compo = 0 
        def dfs(i):
            if i in vis or i > n-1:
                return 
            vis.add(i)
            for j in range(n):
                if j not in vis :
                    if stones[i][0] == stones[j][0] or stones[i][1] == stones[j][1] :
                        dfs(j)
        for i in range(n):
            if i not in vis :
                compo += 1 
                dfs(i)
        return n - compo 
