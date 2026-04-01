# Last updated: 4/1/2026, 3:20:13 PM
# Two Pointer: reduce operation by swapping, not overwriting.
1class Solution:
2    def moveZeroes(self, nums: List[int]) -> None:
3        """
4        Do not return anything, modify nums in-place instead.
5        """
6        next_index = self.removeElement(nums, 0)
7        return nums
8    
9    def removeElement(self, nums, val):
10        slow = fast = 0
11        while fast < len(nums):
12            if nums[fast] != val:
13                if fast > slow:
14                    nums[slow], nums[fast] = nums[fast], nums[slow]
15                slow += 1
16            fast += 1
17        return slow
18