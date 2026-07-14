# Last updated: 7/14/2026, 3:39:39 PM
1class Solution:
2    def removeKdigits(self, num: str, k: int) -> str:
3        if not num or len(num)<=k:
4            return "0"
5        num_stack = []
6
7        for i in range(len(num)):
8            while num_stack and num[i]<num_stack[-1] and k>0:
9                num_stack.pop()
10                k -= 1
11            num_stack.append(num[i])
12        
13        while k>0:
14            num_stack.pop()
15            k -= 1
16        
17        res = "".join(num_stack).lstrip("0")
18        return res if res else "0"
19