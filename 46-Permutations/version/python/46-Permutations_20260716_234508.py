# Last updated: 7/16/2026, 11:45:08 PM
# Backtracking
1"""
2Time: O(n*n!)
3Space: O(n)
4"""
5class Solution:
6    def permute(self, nums: List[int]) -> List[List[int]]:
7        res = []
8        track = []
9        used = [False]*len(nums)
10        def helper(nums, track, used):
11            if len(track) == len(nums):
12                res.append(track.copy())
13                return
14            for i in range(len(nums)):
15                if used[i]:
16                    continue
17                track.append(nums[i])
18                used[i] = True
19                helper(nums, track, used)
20                track.pop()
21                used[i] = False
22        
23        helper(nums, track, used)
24        return res
25