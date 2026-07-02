# Last updated: 7/2/2026, 3:37:14 PM
1class Solution:
2    def decodeString(self, s: str) -> str:
3        decode_stack = []
4        curr_int = 0
5        curr_str = ""
6        for i in range(len(s)):
7            if s[i].isdigit():
8                curr_int = 10*curr_int+int(s[i])
9            elif s[i] == "]":
10                prev_str, curr_int = decode_stack.pop()
11                curr_str = prev_str + curr_int*curr_str
12                curr_int = 0
13            elif s[i] == "[":
14                decode_stack.append((curr_str, curr_int))
15                curr_str = ""
16                curr_int = 0
17            else:
18                curr_str += s[i]
19        return curr_str
20
21