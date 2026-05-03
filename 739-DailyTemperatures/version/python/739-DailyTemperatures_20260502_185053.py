# Last updated: 5/2/2026, 6:50:53 PM
1class Solution:
2    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
3        res = [-1]*len(temperatures)
4        stack = []
5        for i in range(len(temperatures)):
6            while stack and temperatures[i]>stack[-1][0]:
7                prev_temperature, prev_idx = stack.pop()
8                res[prev_idx] = i-prev_idx
9            stack.append((temperatures[i], i))
10
11        while stack:
12            _, idx = stack.pop()
13            res[idx] = 0
14
15        return res
16