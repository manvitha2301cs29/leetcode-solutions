class Solution:
    def maxArea(self, height: list[int]) -> int:
        n = len(height)
        ans = 0 
        l = 0 
        h = n -1 
        maxi = 0 
        while l < h :
            maxi = max(maxi , (h-l)*(min(height[l],height[h])))
            if height[l] <= height[h]:
                l += 1 
            else :
                h -=1 
        return maxi 
