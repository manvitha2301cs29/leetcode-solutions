class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        n = len(fruits)
        i = 0 
        if n == 1 :
            return 1 
        if n == 2 :
            return 2 
        j = 1 
        dic = defaultdict(int)
        dic[fruits[i]] = 1 
        maxi = 0 
        while j < n :
            if fruits[j] in dic :
                dic[fruits[j]] += 1 
            else :   
                dic[fruits[j]] += 1 
                while len(dic) > 2 and i < j  :
                    dic[fruits[i]] -= 1 
                    if dic[fruits[i]] == 0 :
                        del dic[fruits[i]] 
                    i += 1 
            
            maxi = max(maxi,j-i+1)
            j +=  1 
        return maxi 



