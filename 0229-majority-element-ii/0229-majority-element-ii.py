class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n = len(nums)
        cand1 = None 
        cand2 = None 
        res = []
        c1 = 0 
        c2 = 0 
        for i in nums:
            if cand1 == i :
                c1 += 1 
            elif cand2 == i :
                c2 += 1 
            elif c1 == 0 :
                cand1 = i 
                c1 = 1 
            elif c2 == 0 :
                cand2 = i 
                c2 = 1 
            else :
                c1 -= 1 
                c2 -= 1 
        c1 = c2 = 0
        for i in range(n):
            if nums[i] == cand1 :
                c1 += 1 
            elif nums[i] == cand2 :
                c2 += 1 
        if c1 > n//3 :
            res.append(cand1)
        if c2 > n//3 :
            res.append(cand2)
        return res 


        