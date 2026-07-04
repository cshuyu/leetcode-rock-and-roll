# Last updated: 7/4/2026, 12:08:51 AM
1class Solution:
2    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
3        res = []
4        def calculateNextGreatMap(nums):
5            stack = []
6            great_value_dict = {}
7            for i in range(len(nums) - 1, -1, -1):
8                while stack and stack[-1]<nums[i]:
9                    stack.pop()
10                if not stack:
11                    great_value_dict[nums[i]] = -1
12                else:
13                    great_value_dict[nums[i]] = stack[-1]
14                stack.append(nums[i])
15            return great_value_dict
16
17        great_value_dict = calculateNextGreatMap(nums2)
18        for num in nums1:
19            res.append(great_value_dict[num])
20        return res
21
22