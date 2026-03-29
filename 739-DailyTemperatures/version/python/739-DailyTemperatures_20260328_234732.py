# Last updated: 3/28/2026, 11:47:32 PM
# Monotonical Stack
1# Time Complexity: O(n)
2# Space Complexity: O(n)
3class Solution:
4    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
5        stack = []
6        n = len(temperatures)
7        res = [0]*n
8
9        for i in range(n-1, -1, -1):
10            while stack and temperatures[stack[-1]] <= temperatures[i]:
11                stack.pop()
12            if stack:
13                res[i] = stack[-1]-i
14            stack.append(i)
15        
16        return res
17