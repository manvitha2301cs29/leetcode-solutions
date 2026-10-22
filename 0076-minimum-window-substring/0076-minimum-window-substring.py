from collections import Counter 
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        ns = len(s)
        nt = len(t)
        freq = Counter(t)
        haha = defaultdict(int)
        i = 0 
        mini = float('inf')
        si = ""
        for j in range(ns):
            haha[s[j]] += 1 
            while len(haha) >= len(freq) and all(haha[u] >= freq[u] for u in freq.keys()) and i <= j :
                if mini > j - i + 1 :
                    mini = j - i + 1
                    si = s[i:j+1]
                haha[s[i]] -= 1 
                if haha[s[i]] == 0 :
                    del haha[s[i]]
                i += 1 
                
        return si 


