class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        ans =[]
        deq = deque()
        for i in range(n):
            while deq and deq[0]<= i - k :
                deq.popleft()
            while deq and nums[deq[-1]] <= nums[i]:
                deq.pop()
            deq.append(i)
            if i >= k -1 :
                ans.append(nums[deq[0]])
        return ans 