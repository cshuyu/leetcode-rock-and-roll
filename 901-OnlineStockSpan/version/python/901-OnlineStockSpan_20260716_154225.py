# Last updated: 7/16/2026, 3:42:25 PM
1"""
2Time: amortize O(1)
3Space: O(n)
4"""
5class StockSpanner:
6    def __init__(self):
7        self.stock_stack = []
8        self.day = 0
9        self.stock_stack.append([0, 0])
10
11    def next(self, price: int) -> int:
12        self.day += 1
13        while self.stock_stack and price >= self.stock_stack[-1][1]:
14            self.stock_stack.pop()
15        if self.stock_stack:
16            prev_day = self.stock_stack[-1][0]
17        else:
18            prev_day = 0
19        self.stock_stack.append([self.day, price])
20        span = self.day - prev_day
21        return span
22
23        
24
25
26# Your StockSpanner object will be instantiated and called as such:
27# obj = StockSpanner()
28# param_1 = obj.next(price)