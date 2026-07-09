# Last updated: 7/8/2026, 6:11:32 PM
1"""
2Time: O(logn)
3Space:O(1)
4"""
5class Solution:
6    def twoSum(self, numbers: List[int], target: int) -> List[int]:
7        left = 1
8        right = len(numbers)
9        while left<right:
10            if numbers[left-1]+numbers[right-1]<target:
11                left += 1
12            elif numbers[left-1]+numbers[right-1]>target:
13                right -= 1
14            else:
15                return [left, right]
16        return [-1, -1]
17