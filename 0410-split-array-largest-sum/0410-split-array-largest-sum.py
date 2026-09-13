class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        arr = nums
        n = len(arr)
        if k > n :
            return -1 
        low = max(arr)
        high = sum(arr)
        ans = -1 
        
        def possible(x):
            count = 1 
            sumi = arr[0]
            for i in range(1,n):
                if sumi + arr[i] > x :
                    sumi = arr[i]
                    count += 1 
                else :
                    sumi += arr[i]
            return count <= k 
        while low <= high :
            mid = low + (high -low)//2 
            if possible(mid):
                ans = mid 
                high = mid - 1 
            else :
                low = mid + 1 
        return ans
