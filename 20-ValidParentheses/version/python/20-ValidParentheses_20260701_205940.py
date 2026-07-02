# Last updated: 7/1/2026, 8:59:40 PM
# Stack
1class Solution:
2    def isValid(self, s: str) -> bool:
3        char_dict = {"(": ")", "[": "]", "{": "}"}  
4        char_stack = []
5        for i in range(len(s)-1, -1, -1):
6            if s[i] in char_dict.keys():
7                if char_stack:
8                    last_char = char_stack.pop()
9                    if char_dict[s[i]] != last_char:
10                        return False
11                else:
12                    return False
13            else:
14                char_stack.append(s[i])
15
16        if not char_stack:
17            return True
18        else:
19            return False
20        