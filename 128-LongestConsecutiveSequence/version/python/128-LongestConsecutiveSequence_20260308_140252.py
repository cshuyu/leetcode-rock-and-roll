# Last updated: 3/8/2026, 2:02:52 PM
1class Solution:
2    def longestConsecutive(self, nums: List[int]) -> int:
3        num_set = set(nums)
4        max_res = 0
5        for num in num_set:
6            if num-1 in num_set:
7                continue
8            curr_max = 1
9            curr_num = num
10            while curr_num+1 in num_set:
11                curr_num += 1
12                curr_max += 1
13            max_res = max(max_res, curr_max)
14        return max_res