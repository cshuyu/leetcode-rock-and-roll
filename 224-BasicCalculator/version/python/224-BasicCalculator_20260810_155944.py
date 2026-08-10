# Last updated: 8/10/2026, 3:59:44 PM
# Calculator Design: stack
1"""
2Time: O(n)
3Space: O(n)
4"""
5class Solution:
6    def calculate(self, s: str) -> int:
7        i = 0
8
9        def helper():
10            nonlocal i
11            num = 0
12            pre_sign = "+"
13            stack = []
14            while i < len(s):
15                ch = s[i]
16                if ch.isdigit():
17                    num = 10*num+int(ch)
18                if ch == "(":
19                    i += 1
20                    num = helper()
21                if ch in "+-)" or i == len(s)-1:
22                    if pre_sign == "+":
23                        stack.append(num)
24                    elif pre_sign == "-":
25                        stack.append(-num)
26                    if ch == ")":
27                        return sum(stack)
28                    num = 0
29                    pre_sign = ch
30
31                i += 1
32            return sum(stack)
33        
34        return helper()
35        