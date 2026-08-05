# Last updated: 8/5/2026, 3:10:05 PM
# Backtracking: subset(duplication, no_reusable)
1"""
2Time: O(2^n*n)
3Space: O(n)
4"""
5class Solution:
6    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
7        nums.sort()
8        result = []
9        subset = []
10
11        def helper(start):
12            result.append(subset[:])
13            for i in range(start, len(nums)):
14                if i>start and nums[i] == nums[i-1]:
15                    continue
16                subset.append(nums[i])
17                helper(i+1)
18                subset.pop()
19        
20        helper(0)
21        return result
22