# Last updated: 4/4/2026, 4:36:33 PM
# Two Pointers
1
2'''
3Time Complexity: O(n)
4Space Complexity: O(n)
5'''
6class Solution:
7    def sortedSquares(self, nums: List[int]) -> List[int]:
8        res = [0]*len(nums)
9        p1 = 0
10        p2 = p3 = len(nums)-1
11        while p1<=p2:
12            if nums[p1]*nums[p1] <= nums[p2]*nums[p2]:
13                res[p3] = nums[p2]*nums[p2]
14                p3 -= 1
15                p2 -= 1
16            else:
17                res[p3] = nums[p1]*nums[p1]
18                p3 -= 1
19                p1 += 1
20        return res
21
22        