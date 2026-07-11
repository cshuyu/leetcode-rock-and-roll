# Last updated: 7/11/2026, 4:11:08 PM
1class Solution:
2    def searchInsert(self, nums: List[int], target: int) -> int:
3        if not nums:
4            return -1
5        left = 0
6        right = len(nums)-1
7        while left<right-1:
8            mid = left+(right-left)//2
9            # print(f"left:{left}, right:{right}, mid:{mid}, mid_val:{nums[mid]}")
10            if nums[mid] == target:
11                return mid
12            elif nums[mid]<target:
13                left = mid+1
14            else:
15                right = mid
16        # print(f"==left:{left}, right:{right}, mid:{mid}, mid_val:{nums[mid]}")
17        if nums[left]>=target:
18            return left
19        elif target<=nums[right]:
20            return right
21        else:
22            return right+1