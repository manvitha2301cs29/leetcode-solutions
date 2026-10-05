class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        n = len(nums)
        dic = defaultdict(int)
        for i,ni  in enumerate(nums) :
            if target - ni in dic :
                return [dic[target-ni],i]
            else :
                dic[ni] = i 
        return [-1,-1]
        