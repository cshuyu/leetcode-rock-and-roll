# Last updated: 8/6/2026, 12:22:04 AM
# Backtracking: Subsets
1"""
2Time: O(n*2^n)
3Space: O(n)
4"""
5class Solution:
6    def subsets(self, nums: List[int]) -> List[List[int]]:
7        res = []
8        subset = []
9        def helper(start):
10            res.append(subset[:])
11            for i in range(start, len(nums)):
12                subset.append(nums[i])
13                helper(i+1)
14                subset.pop()
15        helper(0)
16        return res 