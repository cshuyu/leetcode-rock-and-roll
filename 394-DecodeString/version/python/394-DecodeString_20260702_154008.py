# Last updated: 7/2/2026, 3:40:08 PM
# Stack
1Time: O(n)
2Space: O(n)
3class Solution:
4    def decodeString(self, s: str) -> str:
5        decode_stack = []
6        curr_int = 0
7        curr_str = ""
8        for i in range(len(s)):
9            if s[i].isdigit():
10                curr_int = 10*curr_int+int(s[i])
11            elif s[i] == "]":
12                prev_str, curr_int = decode_stack.pop()
13                curr_str = prev_str + curr_int*curr_str
14                curr_int = 0
15            elif s[i] == "[":
16                decode_stack.append((curr_str, curr_int))
17                curr_str = ""
18                curr_int = 0
19            else:
20                curr_str += s[i]
21        return curr_str
22
23