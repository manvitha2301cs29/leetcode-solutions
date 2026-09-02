class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        n = len(nums1)
        
        n2 = len(nums2)
        ni = defaultdict(int)
        s = []
        s.append(nums2[-1])
        ni[nums2[-1]] = - 1
        for i in range(n2-2,-1,-1):
            while s and  nums2[i] >= s[-1]:
                s.pop()
            ni[nums2[i]] = -1 if not s else s[-1]
            s.append(nums2[i])
        ans = []
        for i in range(n):
            ans.append(ni[nums1[i]])
        return ans 

