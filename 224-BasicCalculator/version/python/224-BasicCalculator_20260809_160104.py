# Last updated: 8/9/2026, 4:01:04 PM
# Calculator: OOD with stack
1"""
21. Parentheses is the 1st priority;
32. If there are spaces or invalid expression, we just skip;
43. we can add them to the stack to track the "(" and ")"
54. we need to consider the unary condition
6O(Time): O(n)
7O(Space): O(n)
8"""
9class Solution:
10    def calculate(self, s: str) -> int:
11        stack = []
12        result = 0
13        # like sign
14        op = 1
15        # it is used to process two consecutive sign, lik -(-5)
16        unary = 1
17        expect_operand = True
18
19        i = 0
20        n = len(s)
21
22        while i<n:
23            ch = s[i]
24
25            if ch == " ":
26                i += 1
27
28            if ch.isdigit():
29                num = 0
30                while i<n and s[i].isdigit():
31                    num = num*10 + int(s[i])
32                    i += 1
33                result += op * unary * num
34                unary = 1
35                expect_operand = False
36
37            if ch == "+" or ch == "-":
38                if expect_operand:
39                    if ch == "-":
40                        unary *= -1
41                else:
42                    op = 1 if ch == "+" else -1
43                    unary = 1
44                    expect_operand = True
45                i += 1
46            
47            if ch == "(":
48                stack.append((result, op, unary))
49                result = 0
50                op = 1
51                unary = 1
52                expect_operand = True
53
54                i += 1
55                continue
56            
57            if ch == ")":
58                prev_result, prev_op, prev_unary = stack.pop()
59                result = prev_result + prev_op * prev_unary * result
60
61                op = 1
62                unary = 1
63                expect_operand = False
64
65                i += 1
66                continue
67            
68        return result