# Last updated: 3/27/2026, 1:36:35 PM
# Monotonic Stack
1'''
2Time Complexity: O(len(nums2)+len(nums1))
3Space Complexity: O(len(nums2)+len(nums1))
4'''
5class Solution:
6    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
7        n = len(nums2)
8        stack = []
9        greaterMap = defaultdict(int)
10        res = []
11
12        for i in range(n-1, -1, -1):
13            while stack and stack[-1] <= nums2[i]:
14                stack.pop()
15            greaterMap[nums2[i]] = stack[-1] if stack else -1
16            stack.append(nums2[i])
17
18        for num in nums1:
19            res.append(greaterMap[num])
20        return res
21
22        