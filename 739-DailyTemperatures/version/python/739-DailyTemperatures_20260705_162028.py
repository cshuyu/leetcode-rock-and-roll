# Last updated: 7/5/2026, 4:20:28 PM
1class Solution:
2    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
3        # decreasing monotonic stack
4        stack = []
5        res = [0]*len(temperatures)
6        stack.append(0)
7        for i in range(1, len(temperatures)):
8            while stack and temperatures[i]>temperatures[stack[-1]]:
9                idx = stack.pop()
10                res[idx] = i-idx
11            stack.append(i)
12        
13        return res
14
15
16
17
18