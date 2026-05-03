# Last updated: 5/2/2026, 7:02:34 PM
# Monotonic Stack: 2nd Practice
1'''
2Clarification:
31) Input Scale: What should I return if the input list is empty or null?
42) Edge Case: If no warmer day is found, should I return 0, -1, or null?
5'''
6class Solution:
7    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
8        res = [0]*len(temperatures)
9        stack = []
10        for i in range(len(temperatures)):
11            while stack and temperatures[i]>temperatures[stack[-1]]:
12                prev_idx = stack.pop()
13                res[prev_idx] = i-prev_idx
14            stack.append(i)
15
16        return res
17