# Last updated: 7/1/2026, 6:10:31 PM
# stack
1class Solution:
2    def simplifyPath(self, path: str) -> str:
3        dir_lst = path.split("/")
4        stack = []
5        for portion in dir_lst:
6            if portion == "." or portion == "":
7                continue
8            elif portion == "..":
9                if stack:
10                    stack.pop()
11            else:
12                stack.append(portion)
13        
14        res_str = "/" + "/".join(stack)
15        return res_str
16