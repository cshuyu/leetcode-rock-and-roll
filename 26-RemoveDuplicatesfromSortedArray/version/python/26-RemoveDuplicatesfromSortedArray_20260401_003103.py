# Last updated: 4/1/2026, 12:31:03 AM
# Two Pointer
1class Solution:
2    def removeDuplicates(self, nums: List[int]) -> int:
3        slow = 0
4        fast = 0
5        while fast < len(nums):
6            if nums[slow] != nums[fast]:
7                slow += 1
8                nums[slow] = nums[fast]
9            fast += 1
10        
11        return slow+1
12        