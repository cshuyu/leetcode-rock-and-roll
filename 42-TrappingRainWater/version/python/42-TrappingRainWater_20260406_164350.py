# Last updated: 4/6/2026, 4:43:50 PM
# Brute Force with Memoization Optimization
1'''
2O(Time): O(n)
3O(Space): O(n)
4'''
5class Solution:
6    def trap(self, height: List[int]) -> int:
7        n = len(height)
8        lmax = [0]*n
9        rmax = [0]*n
10        lmax[0] = height[0]
11        rmax[n-1] = height[n-1]
12        res = 0
13        for i in range(1, n):
14            lmax[i] = max(lmax[i-1], height[i])
15        for i in range(n-2, -1, -1):
16            rmax[i] = max(rmax[i+1], height[i])
17        for i in range(len(height)):
18            res += min(lmax[i], rmax[i]) - height[i]
19        return res