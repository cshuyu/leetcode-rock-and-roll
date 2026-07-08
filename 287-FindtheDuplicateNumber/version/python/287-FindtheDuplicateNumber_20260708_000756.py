# Last updated: 7/8/2026, 12:07:56 AM
# Two Pointers: cycle
1Time: O(n)
2Space: O(1)
3class Solution:
4    def findDuplicate(self, nums: List[int]) -> int:
5        slow = fast = nums[0]
6        # phase 1: find the intersection
7        while True:
8            slow = nums[slow]
9            fast = nums[nums[fast]]
10            if slow == fast:
11                break
12        # phase 2: find the repeated number
13        slow = nums[0]
14        while slow!=fast:
15            fast = nums[fast]
16            slow = nums[slow]
17        return slow
18        