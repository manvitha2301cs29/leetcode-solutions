class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        i = 0 
        maxi = 0 
        se = set()
        for j in range(n):
            if s[j] not  in se :
                se.add(s[j])
            else :
                while s[j] in se and i <j :
                    se.remove(s[i])
                    i += 1
                se.add(s[j])
            maxi = max(maxi,j-i+1)
        return maxi 