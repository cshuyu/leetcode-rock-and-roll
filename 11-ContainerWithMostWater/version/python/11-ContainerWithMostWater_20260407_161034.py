# Last updated: 4/7/2026, 4:10:34 PM
# Two Pointers with water tank
1'''
2Time Complexity: O(n)
3Space Complexity: O(1)
4'''
5class Solution:
6    def maxArea(self, height: List[int]) -> int:
7        left = 0
8        right = len(height)-1
9        res = 0
10        while left<right:
11            curr_area = min(height[left], height[right])*(right-left)
12            res = max(res, curr_area)
13            if height[left] < height[right]:
14                left += 1
15            else:
16                right -= 1
17        return res