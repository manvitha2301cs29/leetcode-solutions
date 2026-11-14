class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        n = len(asteroids)
        s = []
         
        s.append(asteroids[-1])
        for i in range(n-2,-1,-1):
            a = asteroids[i]
            dontadd = False
            while s and s[-1] < 0 and a > 0 :
                if a > abs(s[-1]) :
                    s.pop()
                elif a < abs(s[-1]) :
                    dontadd = True 

                    break 
                else :
                    s.pop()
                    dontadd = True 
                    break

            if not dontadd :
                s.append(a)
                
        s.reverse()
        return s
                
                
        
