# Last updated: 8/19/2026, 12:11:04 AM
# Greedy Algorithm: non-overlapping(sort by end)
1"""
2Time: O(nlogn)
3Space: O(n)
4"""
5class Solution:
6    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
7        intervals.sort(key=lambda x: x[1])
8        remove_count = 0
9        if not intervals:
10            return 0
11        prev_end = intervals[0][1]
12        for interval in intervals[1:]:
13            if interval[0]<prev_end:
14                remove_count += 1
15            else:
16                prev_end = interval[1]
17        
18        return remove_count