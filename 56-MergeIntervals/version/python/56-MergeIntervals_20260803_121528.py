# Last updated: 8/3/2026, 12:15:28 PM
# Greedy algorithm
1"""
2Time: O(nlogn)
3Space: O(n)
4"""
5class Solution:
6    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
7        if not intervals:
8            return []
9        intervals.sort(key=lambda x: x[0])
10        merged = [intervals[0]]
11
12        for start, end in intervals[1:]:
13            last_start, last_end = merged[-1]
14            if start <= last_end:
15                merged[-1][1] = max(last_end, end)
16            else:
17                merged.append([start, end])
18        return merged
19