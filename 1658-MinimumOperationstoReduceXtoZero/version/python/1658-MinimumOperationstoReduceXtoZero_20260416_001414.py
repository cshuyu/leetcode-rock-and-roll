# Last updated: 4/16/2026, 12:14:14 AM
# Sliding window
1class Solution:
2    def minOperations(self, nums: List[int], x: int) -> int:
3        target = sum(nums)-x
4        left = right = 0
5        total = 0
6        max_len = -1
7        while right<len(nums):
8            total += nums[right]
9            right += 1
10            while total>target and left<right:
11                total -= nums[left]
12                left += 1
13            if total == target:
14                max_len = max(max_len, right-left)
15        return -1 if max_len==-1 else len(nums)-max_len