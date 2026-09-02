class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        MOD = 10**9 +7 
        ans = 0 
        n = len(arr)
        pse = [-1]*n 
        nse = [n]*n 
        s = []
        for i in range(n-1,-1,-1):
            while s and arr[i] <= arr[s[-1]]:
                s.pop()
            nse[i] = n if not s else s[-1]
            s.append(i)
        s = []
        for i in range(n):
            while s and arr[i] < arr[s[-1]] :
                s.pop()
            pse[i] = -1 if not s else s[-1]
            s.append(i)
        for  i in range(n):
            ans += (i - pse[i])*(nse[i] - i)*arr[i]
        return ans%MOD
        