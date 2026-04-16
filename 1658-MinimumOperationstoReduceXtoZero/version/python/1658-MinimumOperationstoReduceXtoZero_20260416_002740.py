# Last updated: 4/16/2026, 12:27:40 AM
1class Solution:
2    def minOperations(self, nums: List[int], x: int) -> int:
3        target = sum(nums)-x
4        if target<0:
5            return -1
6        left = right = 0
7        total = 0
8        max_len = -1
9        while right<len(nums):
10            total += nums[right]
11            right += 1
12            while total>target:
13                total -= nums[left]
14                left += 1
15            if total == target:
16                max_len = max(max_len, right-left)
17        return -1 if max_len==-1 else len(nums)-max_len