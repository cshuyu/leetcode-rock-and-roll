# Last updated: 4/1/2026, 1:12:04 PM
# Two Pointer with move zero
1class Solution:
2    def removeElement(self, nums: List[int], val: int) -> int:
3        slow = 0
4        fast = 0
5        while fast<len(nums):
6            if nums[fast] != val:
7                nums[slow] = nums[fast]
8                slow += 1
9            fast += 1
10        return slow
11
12
13