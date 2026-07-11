# Last updated: 7/11/2026, 3:05:40 PM
# Binary Search
1"""
2Time: O(logn)
3Space: O(1)
4"""
5class Solution:
6    def search(self, nums: List[int], target: int) -> int:
7        if not nums:
8            return -1
9        left = 0
10        right = len(nums)-1
11        while left<=right:
12            mid = left + (right-left)//2
13            if nums[mid] == target:
14                return mid
15            # left part hasn't been rotated
16            if nums[mid]>=nums[left]:
17                if nums[left]<=target<nums[mid]:
18                    right = mid-1
19                else:
20                    left = mid+1
21            # right part hasn't been rotated
22            else:
23                if nums[mid]<target<=nums[right]:
24                    left = mid+1
25                else:
26                    right = mid-1
27        return -1
28