class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        n = len(num)
        s = []
        if k >= n :
            return "0"
        for i in range(n):
             
            while s and num[i] < s[-1] and k >0 :
                s.pop()
                k -=1 
            s.append(num[i])
        while k > 0 :
            s.pop()
            k -= 1
        si = "".join(s).lstrip("0")
        return si if si else "0"


        