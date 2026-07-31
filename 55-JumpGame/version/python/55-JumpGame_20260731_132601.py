# Last updated: 7/31/2026, 1:26:01 PM
# Greedy Algorithm
1"""
2Time: O(n)
3Space: O(1)
4"""
5class Solution:
6    def canJump(self, nums: List[int]) -> bool:
7        farthest = 0
8        for i in range(len(nums)):
9            if i > farthest:
10                return False
11            farthest = max(farthest, i+nums[i])
12            if farthest >= len(nums)-1:
13                return True
14        return False