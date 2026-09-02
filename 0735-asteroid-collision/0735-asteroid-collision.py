class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        n = len(asteroids)
        s = []
        dontadd = False 
        for a in asteroids :
            dontadd = False 
            while s and s[-1] > 0 and a < 0 :
                if abs(a) > s[-1] :
                    s.pop()
                elif abs(a) < s[-1] :
                    dontadd = True 
                    break 
                else :
                    s.pop()
                    dontadd = True
                    break
            if not dontadd :
                s.append(a)
            
        return s 
        
