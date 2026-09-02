class Solution:
    def trap(self, height: List[int]) -> int:
        # at ith index water stored is min(max_left_height ,max_right_height ) - curr_height
        n = len(height)
        lm = l = 0 
        rm = r = n -1 
        ans = 0 
        while l <= r :
            if height[l] <= height[r]:
                if height[lm] < height[l]:
                    lm = l 
                else :
                    ans += max(0,height[lm] -height[l] )
                l += 1 
            else :
                if height[rm] < height[r]:
                    rm = r
                else :
                    ans += max(0,height[rm] -height[r] )
                r -=1
        return ans 
