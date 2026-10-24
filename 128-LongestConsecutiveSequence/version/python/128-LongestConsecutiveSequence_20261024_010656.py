# Last updated: 10/24/2026, 1:06:56 AM
# HashSet
1"""
2Time: O(n)
3Sapce: O(n)
4"""
5class Solution:
6    def longestConsecutive(self, nums: list[int]) -> int:
7        if not nums:
8            return 0
9        num_set = set(nums)
10        max_count = 0
11        for i in num_set:
12            curr_num = i
13            if curr_num-1 not in num_set:
14                count = 1
15                while curr_num+1 in num_set:
16                    curr_num += 1
17                    count += 1
18                max_count = max(max_count, count)
19        return max_count