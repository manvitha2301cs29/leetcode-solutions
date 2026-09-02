class StockSpanner:

    def __init__(self):
        self.s = []
        self.indx = 0 
        

    def next(self, price: int) -> int:
        
        count = 0 
        while self.s and price >= self.s[-1][0] :
            self.s.pop()
        count = self.indx + 1 if not self.s else self.indx - self.s[-1][1]
        self.s.append((price,self.indx))
        self.indx += 1 
        return count 


        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)