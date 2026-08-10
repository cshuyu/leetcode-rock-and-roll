# Last updated: 8/10/2026, 3:58:33 PM
1class Solution:
2    def calculate(self, s: str) -> int:
3        i = 0
4
5        def helper():
6            nonlocal i
7            num = 0
8            pre_sign = "+"
9            stack = []
10            while i < len(s):
11                ch = s[i]
12                if ch.isdigit():
13                    num = 10*num+int(ch)
14                if ch == "(":
15                    i += 1
16                    num = helper()
17                if ch in "+-)" or i == len(s)-1:
18                    if pre_sign == "+":
19                        stack.append(num)
20                    elif pre_sign == "-":
21                        stack.append(-num)
22                    if ch == ")":
23                        return sum(stack)
24                    num = 0
25                    pre_sign = ch
26
27                i += 1
28            return sum(stack)
29        
30        return helper()
31        