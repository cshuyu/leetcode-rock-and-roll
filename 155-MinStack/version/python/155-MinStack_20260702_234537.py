# Last updated: 7/2/2026, 11:45:37 PM
1Time: O(1)
2Space: O(n)
3class MinStack:
4
5    def __init__(self):
6        self.num_stack = []
7
8    def push(self, value: int) -> None:
9        if not self.num_stack:
10            self.num_stack.append((value, value))
11        else:
12            _, curr_min = self.num_stack[-1]
13            self.num_stack.append((value, min(curr_min, value)))
14
15    def pop(self) -> None:
16        val, _ = self.num_stack.pop()
17        return val
18
19    def top(self) -> int:
20        return self.num_stack[-1][0]
21
22    def getMin(self) -> int:
23        return self.num_stack[-1][1]
24
25
26# Your MinStack object will be instantiated and called as such:
27# obj = MinStack()
28# obj.push(value)
29# obj.pop()
30# param_3 = obj.top()
31# param_4 = obj.getMin()
32
33