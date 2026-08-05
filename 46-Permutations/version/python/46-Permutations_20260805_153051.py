# Last updated: 8/5/2026, 3:30:51 PM
# Backtracking: permutation(no_duplicate&no_resuable)
1"""
2Time: O(n*n!)
3Space: O(n)
4"""
5class Solution:
6    def permute(self, nums: List[int]) -> List[List[int]]:
7        res = []
8        used = [False]*len(nums)
9
10        def helper(path):
11            if len(path) == len(nums):
12                res.append(path[:])
13                return
14
15            for i in range(len(nums)):
16                if used[i]:
17                    continue
18
19                used[i] = True
20                path.append(nums[i])
21
22                helper(path)
23
24                path.pop()
25                used[i] = False
26
27        helper([])
28        return res