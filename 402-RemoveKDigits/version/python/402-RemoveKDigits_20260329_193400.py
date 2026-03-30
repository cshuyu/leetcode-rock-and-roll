# Last updated: 3/29/2026, 7:34:00 PM
# Monotonic Stack
1'''
2Time and Space complexity are both O(n)
3'''
4class Solution:
5    def removeKdigits(self, num: str, k: int) -> str:
6        stack = []
7
8        for i in range(len(num)):
9            while stack and stack[-1] > num[i] and k>0:
10                stack.pop()
11                k -= 1
12            stack.append(num[i])
13
14        while k>0:
15            stack.pop()
16            k -= 1
17        
18        res = "".join(stack).lstrip('0')
19        return res if res else "0"