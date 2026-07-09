# Last updated: 7/9/2026, 1:52:06 PM
# Bucket Sort
1"""
2Time: O(n)
3Space: O(1)
4The left pointer points to the next position of 0;
5The right pointer points to the next position of 2;
6The space between the pointer left and mid is the area of 1;
7However the space between the mid and right pointer is unknown area. 
8"""
9class Solution:
10    def sortColors(self, nums: List[int]) -> None:
11        """
12        Do not return anything, modify nums in-place instead.
13        """
14        left = mid = 0
15        right = len(nums)-1
16        while mid<=right:
17            if nums[mid]==0:
18                nums[mid], nums[left] = nums[left], nums[mid]
19                mid += 1
20                left += 1
21            elif nums[mid]==1:
22                mid += 1
23            else:
24                nums[mid], nums[right] = nums[right], nums[mid]
25                right -= 1
26