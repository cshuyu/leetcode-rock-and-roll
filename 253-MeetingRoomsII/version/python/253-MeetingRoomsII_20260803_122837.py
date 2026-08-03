# Last updated: 8/3/2026, 12:28:37 PM
# Greedy Algorithm
1"""
2Time: O(nlogn)
3Space: O(n)
4"""
5class Solution:
6    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
7        if not intervals:
8            return 0
9        intervals.sort(key=lambda x: x[0])
10
11        min_heap = []
12        for start, end in intervals:
13            if min_heap and min_heap[0]<=start:
14                heapq.heappop(min_heap)
15            heapq.heappush(min_heap, end)
16        return len(min_heap)
17