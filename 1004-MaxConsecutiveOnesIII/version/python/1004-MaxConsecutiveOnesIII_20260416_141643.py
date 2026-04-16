# Last updated: 4/16/2026, 2:16:43 PM
# Sliding Window
1class Solution:
2    def longestOnes(self, nums: List[int], k: int) -> int:
3        left = right = 0
4        one_count = 0
5        max_length = 0
6        while right<len(nums):
7            if nums[right]==1:
8                one_count += 1
9            right += 1
10            while right-left-one_count>k:
11                if nums[left] == 1:
12                    one_count -= 1
13                left += 1
14            max_length = max(max_length, right-left)
15        return max_length
16
17
18        