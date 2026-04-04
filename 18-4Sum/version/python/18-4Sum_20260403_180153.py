# Last updated: 4/3/2026, 6:01:53 PM
# Two Pointers with Find N Sum
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
29            for i in range(start, len(nums)):
30                if i>start and nums[i]==nums[i-1]:
31                    continue
32                element = nums[i]
33                combs = self.findNSum(nums, n-1, i+1, target-element)
34                for comb in combs:
35                    comb.append(element)
36                    res.append(comb)
37        return res
38
39
40
41
42            
43
44        