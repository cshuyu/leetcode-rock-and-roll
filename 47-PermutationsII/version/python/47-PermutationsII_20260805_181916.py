# Last updated: 8/5/2026, 6:19:16 PM
# Backtracking: Permutation(duplicate & no_reusable)
1"""
2Time: O(n*n!)
3Space: O(n)
4"""
5class Solution:
6    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
7        res = []
8        permutation = []
9        used = [False]*len(nums)
10        nums.sort()
11        def helper(permutation):
12            if len(permutation) == len(nums):
13                res.append(permutation[:])
14                return
15            for i in range(len(nums)):
16                if used[i]:
17                    continue
18                if i>0 and nums[i]==nums[i-1] and not used[i-1]:
19                    continue
20                permutation.append(nums[i])
21                used[i] = True
22                helper(permutation)
23                permutation.pop()
24                used[i] = False
25        helper([])
26        return res
27
28        