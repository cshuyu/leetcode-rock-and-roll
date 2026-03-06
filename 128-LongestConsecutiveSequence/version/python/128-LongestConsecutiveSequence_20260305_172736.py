# Last updated: 3/5/2026, 5:27:36 PM
# HashSet
1class Solution:
2    def longestConsecutive(self, nums: List[int]) -> int:
3        nums_set = set(nums)
4        max_cnt = 0
5        # It should be nums_set, not nums, otherwise will time exceed
6        for num in nums_set:
7            if (num-1) not in nums_set:
8                curr_cnt = 1
9                curr_num = num
10                while (curr_num+1) in nums_set:
11                    curr_num += 1
12                    curr_cnt += 1
13                max_cnt = max(max_cnt, curr_cnt)
14        return max_cnt
15
16