# Last updated: 7/9/2026, 1:31:35 AM
# Two_pointers: n-sum problem
1"""
2O(Time): O(n^2): max(n^2, nlogn)
3O(Space): O(n)
4"""
5class Solution:
6    def threeSum(self, nums: list[int]) -> list[list[int]]:
7        nums.sort()
8        res = []
9        i = 0
10        while i<len(nums):
11            first = nums[i]
12            pairs = self.twoSum(i+1, nums, -nums[i])
13            for pair in pairs:
14                res.append([first, pair[0], pair[1]])
15            # avoid duplicated elements
16            while i<len(nums) and first==nums[i]:
17                i += 1
18        return res
19
20    def twoSum(self, startIdx, nums, target):
21        left = startIdx
22        right = len(nums)-1
23        pairs = []
24        while left<right:
25            curr_sum = nums[left]+nums[right]
26            if target > curr_sum:
27                left += 1
28            elif target < curr_sum:
29                right -= 1
30            else:
31                left_val = nums[left]
32                right_val = nums[right]
33                pairs.append([left_val, right_val])
34                while left<right and nums[left]==left_val:
35                    left += 1
36                while left<right and nums[right]==right_val:
37                    right -= 1
38        return pairs
39