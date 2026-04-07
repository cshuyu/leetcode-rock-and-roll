# Last updated: 4/6/2026, 5:44:53 PM
# Two Pointer with tank water
1'''
2O(Time): O(n)
3O(Space): O(1)
4'''
5class Solution:
6    def trap(self, height: List[int]) -> int:
7        n = len(height)
8        lmax = 0
9        rmax = 0
10        res = 0
11        left = 0
12        right = n-1
13        while left<right:
14            lmax = max(height[left], lmax)
15            rmax = max(height[right], rmax)
16            if lmax<rmax:
17                res += lmax-height[left]
18                left += 1
19            else:
20                res += rmax-height[right]
21                right -=1
22        return res