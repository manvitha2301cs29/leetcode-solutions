class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        nr = len(ransomNote)
        nm = len(magazine)
        if nr > nm :
            return False 
        fr = Counter(ransomNote)
        fm = Counter(magazine)
        for u in fr.keys():
            if u not in fm :
                return False 
        
        for u,v in fm.items():
            if u in fr and fr[u] > v :
                return False 
        return True