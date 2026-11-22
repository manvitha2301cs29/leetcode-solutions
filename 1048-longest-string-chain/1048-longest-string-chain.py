class Solution:
    def longestStrChain(self, words: list[str]) -> int:
        words.sort(key = lambda x: len(x))
        n = len(words)
        dic = {}
        maxi = 0 
        for w in words :
            dic[w] = 1 
            for i in range(len(w)):
                new = w[:i] + w[i+1:]
                if new in dic :
                    if dic[w] < 1 + dic[new]:
                        dic[w] = 1 + dic[new]
            maxi = max(maxi , dic[w])
        return maxi 
