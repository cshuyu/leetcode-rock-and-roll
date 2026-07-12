# Last updated: 7/11/2026, 10:37:18 PM
# Binary Search
1class Solution:
2    def findMin(self, nums: List[int]) -> int:
3        left = 0
4        right = len(nums)-1
5        if nums[left]<=nums[right]:
6            return nums[left]
7        # left>right
8        while left<right:
9            mid = left + (right-left)//2
10            # print(f"left:{left}, right:{right}, mid:{mid}, mid_val:{nums[mid]}")
11            # the part between mid(exclusively) and right is rotated
12            if nums[mid]>nums[right]:
13                left = mid+1
14            # the part between left and mid(inclusively) is rotated
15            else:
16                right = mid
17        # print(f"==left:{left}, right:{right}")
18        return nums[right]
19