# Last updated: 5/13/2026, 4:14:07 PM
# Two Pointers
1class Solution:
2    def removeDuplicates(self, nums: List[int]) -> int:
3        left = right = 0
4        count = 1
5        while right<len(nums):
6            if nums[left]!= nums[right]:
7                left += 1
8                nums[left] = nums[right]
9                count =1
10            elif left<right and count<2:
11                left += 1
12                nums[left] = nums[right]
13                count += 1
14            right += 1
15        return left+1
16
17
18
19