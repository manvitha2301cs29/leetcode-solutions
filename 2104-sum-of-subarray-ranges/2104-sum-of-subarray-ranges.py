class Solution:
    def subArrayRanges(self, num: list[int]) -> int:
        
        def small(nums):
            n = len(nums)
            nse = [n for i in range(n)]
            pse = [-1 for i in range(n)]
            s  = []
            for i in range(n-1,-1,-1):
                while s and nums[i] < nums[s[-1]] :
                    s.pop()
                nse[i] = s[-1] if s else n 
                s.append(i)
            s = []
            sumi = 0 
            for i in range(n):
                while s and nums[i] <= nums[s[-1]] : 
                    s.pop()
                pse[i] = s[-1] if s else -1 
                s.append(i)
            for i , ni in enumerate(nums) :
                sumi += ni*(i - pse[i])*(nse[i] - i)
            return sumi 
        neg = [-1*ni for ni in num]
        nega = small(neg)
        pos = small(num)
        return -1*nega - pos 
