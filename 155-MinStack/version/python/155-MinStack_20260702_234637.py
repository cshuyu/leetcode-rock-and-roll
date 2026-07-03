# Last updated: 7/2/2026, 11:46:37 PM
1Time: O(1)
2Space: O(n)
3class MinStack:
4
5    def __init__(self):
6        self.num_stack = []
7        self.min_stack = []
8
9    def push(self, value: int) -> None:
10        self.num_stack.append(value)
11        # Only push to min_stack if it's empty or value is a NEW minimum
12        if not self.min_stack or value <= self.min_stack[-1]:
13            self.min_stack.append(value)
14
15    def pop(self) -> None:
16        # If the value we are removing is the current minimum, pop it from min_stack too
17        if self.num_stack.pop() == self.min_stack[-1]:
18            self.min_stack.pop()
19
20    def top(self) -> int:
21        return self.num_stack[-1]
22
23    def getMin(self) -> int:
24        return self.min_stack[-1]
25
26
27# Your MinStack object will be instantiated and called as such:
28# obj = MinStack()
29# obj.push(value)
30# obj.pop()
31# param_3 = obj.top()
32# param_4 = obj.getMin()
33
34