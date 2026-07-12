# Last updated: 7/11/2026, 10:37:33 PM
1class Solution:
2    def findMin(self, nums: List[int]) -> int:
3        left = 0
4        right = len(nums)-1
5        if nums[left]<=nums[right]:
6            return nums[left]
7        # left>right
8        while left<right:
9            mid = left + (right-left)//2
10            # the part between mid(exclusively) and right is rotated
11            if nums[mid]>nums[right]:
12                left = mid+1
13            # the part between left and mid(inclusively) is rotated
14            else:
15                right = mid
16        return nums[left]
17