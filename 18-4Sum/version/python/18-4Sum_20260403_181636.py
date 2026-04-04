# Last updated: 4/3/2026, 6:16:36 PM
# Two Pointers with N sum
1class Solution:
2    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
3        nums.sort()
4        return self.findNSum(nums, 4, 0, target)
5
6    def findNSum(self, nums, n, start, target):
7        res = []
8        if n<2 or n>len(nums):
9            return res
10        if n==2:
11            left = start
12            right = len(nums)-1
13            while left<right:
14                leftVal=nums[left]
15                rightVal=nums[right]
16                if nums[left]+nums[right]<target:
17                    while left<right and nums[left]==leftVal:
18                        left += 1
19                elif nums[left]+nums[right]>target:
20                    while left<right and nums[right]==rightVal:
21                        right -= 1
22                else:
23                    res.append([leftVal, rightVal])
24                    while left<right and nums[left]==leftVal:
25                        left += 1
26                    while left<right and nums[right]==rightVal:
27                        right -= 1
28        else:
29            i = start
30            while i<len(nums):
31                element = nums[i]
32                combs = self.findNSum(nums, n-1, i+1, target-element)
33                for comb in combs:
34                    comb.append(element)
35                    res.append(comb)
36                while i<len(nums) and nums[i] == element:
37                    i += 1
38        return res
39      