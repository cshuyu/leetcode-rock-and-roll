# Last updated: 8/10/2026, 3:24:52 PM
1"""
2Go through the string:
3meet the digits, transfer to the digits:
4 num = num*10+int(char)
5
6meet the signs, we need to analyze case by case:
7 prev_sign == "+-"  ==> stack.append(sign*num) until we meet the next sign and update the prev sign, num=0.
8 prev_sign == "*/" ==> stack.pop() * or / num, append it into the stack and update the prev sign, num=0.
9 if it is the last element ==> calculate prev_sign and num, append into the stack.
10
11parentheses:
12 ch == "(" ==> i+1 call helper() function to calculate the inside of ()
13 ch == ")" ==> return sum(stack)
14 """
15class Solution:
16    def calculate(self, s: str):
17        i = 0
18
19        def helper():
20            nonlocal i
21            stack = []
22            num = 0
23            prev_sign = "+"
24
25            while i<len(s):
26                ch = s[i]
27                if ch.isdigit():
28                    num = num*10+int(s[i])
29                if ch == "(":
30                    i += 1
31                    num = helper()
32                if ch in "+-*/)" or i==len(s)-1:
33                    if prev_sign == "+":
34                        stack.append(num)
35                    elif prev_sign == "-":
36                        stack.append(-num)
37                    elif prev_sign == "*":
38                        stack.append(stack.pop()*num)
39                    elif prev_sign == "/":
40                        stack.append(int(stack.pop()/num))
41                    if ch == ")":
42                        return sum(stack)
43                    
44                    num = 0
45                    prev_sign = ch
46
47                i += 1
48            return sum(stack)
49    
50        return helper()
51
52