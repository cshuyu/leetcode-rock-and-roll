# Last updated: 8/3/2026, 1:29:17 PM
# Greedy Algorithm
1"""
2Time: O(nlogn)
3Space: O(n)
4"""
5class Solution:
6    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
7        intervals.sort(key=lambda x: (x[0], -x[1]))
8        count = 0
9        max_end = 0 
10
11        for start, end in intervals:
12            if end > max_end:
13                count += 1
14                max_end = end
15            
16        return count