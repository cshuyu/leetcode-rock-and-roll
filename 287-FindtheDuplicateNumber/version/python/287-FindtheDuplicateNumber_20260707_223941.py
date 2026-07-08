# Last updated: 7/7/2026, 10:39:41 PM
# Binary Search
1class Solution:
2    def findDuplicate(self, nums: List[int]) -> int:
3        left = 1
4        right = len(nums)-1
5        while left<right:
6            count = 0
7            mid = left+(right-left)//2
8            for num in nums:
9                if num<=mid:
10                    count += 1
11            if count<=mid:
12                left = mid+1
13            else:
14                right = mid
15        return left
16
17        
18