# Last updated: 4/2/2026, 6:54:50 PM
# Two Pointer: three sum
1'''
2Time Complexity: O(n*n) + O(nlogn) = O(n^2)
3Space Complexity: sort will use O(n)
4'''
5class Solution:
6    def threeSum(self, nums: list[int]) -> list[list[int]]:
7        nums.sort()
8        i = 0
9        res = []
10        while i<len(nums):
11            first = nums[i]
12            twoSum = -nums[i]
13            pairLst = self.twoSumPairs(nums, i+1, twoSum)
14            for second, third in pairLst:
15                res.append([first, second, third])
16            while i<len(nums) and nums[i] == first:
17                i += 1
18        return res
19    
20    def twoSumPairs(self, nums, startIndex, target):
21        left = startIndex
22        right = len(nums)-1
23        pairs = []
24        while left<right:
25            leftVal = nums[left]
26            rightVal = nums[right]
27            if nums[left]+nums[right]<target:
28                while left<right and nums[left] == leftVal:
29                    left += 1
30            elif nums[left]+nums[right]>target:
31                while left<right and nums[right] == rightVal:
32                    right -= 1
33            else:
34                pairs.append((leftVal, rightVal))
35                while left<right and nums[left] == leftVal:
36                    left += 1
37                while left<right and nums[right] == rightVal:
38                    right -= 1
39        return pairs
40