class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        d = len(digits)
        dic = {"2" : "abc" , "3" : "def" ,"4" : "ghi","5" : "jkl" ,"6" : "mno" ,"7":"pqrs" , "8" : "tuv","9" : "wxyz"}

        res = []
        def solve(i,path):
            if i == d :
                res.append("".join(path.copy()))
                return 
            ch = digits[i]
            for c in dic[ch]:
                path.append(c)
                solve(i+1,path)
                path.pop()
            
        solve(0,[])
        return res 