# Last updated: 4/4/2026, 3:54:42 PM
# Three Pointers with three way partition
1class Solution:
2    def sortColors(self, nums: List[int]) -> None:
3        """
4        Do not return anything, modify nums in-place instead.
5        """
6        p0 = curr = 0
7        p2 = len(nums)-1
8        while curr<=p2:
9            if nums[curr] == 0:
10                nums[curr], nums[p0] = nums[p0], nums[curr]
11                p0 += 1
12                curr += 1
13            elif nums[curr] == 2:
14                nums[curr], nums[p2] = nums[p2], nums[curr]
15                p2 -= 1
16            else:
17                curr += 1  
18
19        