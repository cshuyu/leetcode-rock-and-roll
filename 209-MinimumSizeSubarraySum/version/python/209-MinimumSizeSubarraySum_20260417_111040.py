# Last updated: 4/17/2026, 11:10:40 AM
# Sliding Window with minimum window size
1class Solution:
2    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
3        left = right = 0
4        sum = 0
5        min_length = float("inf")
6        while right<len(nums):
7            sum += nums[right]
8            right += 1
9            while sum>=target:
10                min_length = min(min_length, right-left)
11                sum -= nums[left]
12                left += 1
13        return min_length if min_length!=float("inf") else 0