# Last updated: 4/1/2026, 2:32:27 PM
# Two pointer
1class Solution:
2    def moveZeroes(self, nums: List[int]) -> None:
3        """
4        Do not return anything, modify nums in-place instead.
5        """
6        next_index = self.removeElement(nums, 0)
7        for i in range(next_index, len(nums)):
8            nums[i] = 0
9        return nums
10    
11    def removeElement(self, nums, val):
12        slow = fast = 0
13        while fast < len(nums):
14            if nums[fast] != val:
15                nums[slow] = nums[fast]
16                slow += 1
17            fast += 1
18        return slow
19
20