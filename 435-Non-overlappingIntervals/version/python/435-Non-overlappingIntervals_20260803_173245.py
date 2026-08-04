# Last updated: 8/3/2026, 5:32:45 PM
# Greedy Algorithm
1"""
2Time: O(nlogn)
3Space: O(n)
4"""
5class Solution:
6    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
7        if not intervals:
8            return 0
9        intervals.sort(key=lambda x: x[1])
10        count = 0
11        prev_end = intervals[0][1]
12
13        for start, end in intervals[1:]:
14            if start < prev_end:
15                count += 1
16            else:
17                prev_end = end
18        
19        return count
20