# Last updated: 7/4/2026, 12:09:42 AM
# Monotonic Stack
1"""
2Time: amortized O(1), totally O(n)
3Space: O(n)
4"""
5class Solution:
6    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
7        res = []
8        def calculateNextGreatMap(nums):
9            stack = []
10            great_value_dict = {}
11            for i in range(len(nums) - 1, -1, -1):
12                while stack and stack[-1]<nums[i]:
13                    stack.pop()
14                if not stack:
15                    great_value_dict[nums[i]] = -1
16                else:
17                    great_value_dict[nums[i]] = stack[-1]
18                stack.append(nums[i])
19            return great_value_dict
20
21        great_value_dict = calculateNextGreatMap(nums2)
22        for num in nums1:
23            res.append(great_value_dict[num])
24        return res
25
26