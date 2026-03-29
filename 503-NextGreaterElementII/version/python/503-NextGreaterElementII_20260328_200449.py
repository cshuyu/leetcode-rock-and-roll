# Last updated: 3/28/2026, 8:04:49 PM
# Circular Monotonic Stack
1# Time Complexity: O(n)
2# Space Complexity: O(n)
3class Solution:
4    def nextGreaterElements(self, nums: List[int]) -> List[int]:
5        stack = []
6        n = len(nums)
7        res = [-1]*n
8        for i in range(2*n-1, -1, -1):
9            curr_num = nums[i%n]
10            while stack and stack[-1]<=curr_num:
11                stack.pop()
12            if i<n and stack:
13                res[i] = stack[-1]
14            stack.append(curr_num)
15        
16        return res