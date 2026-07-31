# Last updated: 7/31/2026, 1:58:39 PM
# Greedy_algorithm
1"""
2Time: O(n)
3Space: O(1)
4"""
5class Solution:
6    def jump(self, nums: List[int]) -> int:
7        n = len(nums)
8        if n == 0:
9            return 0
10        jumps = 0
11        current_end = 0
12        farthest = 0
13
14        for i in range(n-1):
15            farthest = max(farthest, i+nums[i])
16            if i==current_end:
17                jumps += 1
18                current_end = farthest
19            if current_end >= n-1:
20                break
21        
22        return jumps