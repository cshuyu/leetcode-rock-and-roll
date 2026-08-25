# Last updated: 8/25/2026, 2:17:03 PM
# Greedy: maximum non-overlapping
1"""
2It is a maximum of non-overlapping
3Time: O(nlogn)
4space: O(n)
5"""
6class Solution:
7    def findMinArrowShots(self, points: List[List[int]]) -> int:
8        points.sort(key=lambda x: x[1])
9        end = points[0][1]
10        count = 1
11        for i in range(1, len(points)):
12            if points[i][0] > end:
13                count += 1
14                end = points[i][1]
15        return count