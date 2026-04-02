# Last updated: 4/1/2026, 5:19:03 PM
# Two Pointers: Two Sum of Sorted List
1class Solution:
2    def twoSum(self, numbers: List[int], target: int) -> List[int]:
3        left = 0
4        right = len(numbers)-1
5        while left<right:
6            sum = numbers[left]+numbers[right]
7            if sum < target:
8                left += 1
9            elif sum > target:
10                right -= 1
11            else:
12                return [left+1, right+1]
13        return [-1, -1]