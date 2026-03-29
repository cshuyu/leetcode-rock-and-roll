# Last updated: 3/29/2026, 12:25:34 PM
# Monotonic Stack
1class StockPoint:
2    def __init__(self, price, age):
3        self.price = price
4        self.age = age
5
6'''
7Time Complexity: worst O(n), amortize O(1)
8Space Complexity: O(n)
9'''
10class StockSpanner:
11    def __init__(self):
12        self.stack: List[StockPoint] = []
13
14    def next(self, price: int) -> int:
15        age = 1
16        while self.stack and self.stack[-1].price <= price:
17            age += self.stack.pop().age
18        self.stack.append(StockPoint(price, age))
19        return age
20            
21
22        
23
24
25# Your StockSpanner object will be instantiated and called as such:
26# obj = StockSpanner()
27# param_1 = obj.next(price)