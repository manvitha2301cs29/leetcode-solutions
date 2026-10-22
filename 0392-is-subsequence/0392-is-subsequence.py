class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i = 0 
        j = 0 
        ns = len(s)
        nt = len(t)
        if nt < ns :
            return False
        while i < ns and j < nt :
            if s[i] == t[j]:
                i +=1 
                j += 1 
            else:
                j += 1 
        return i == ns