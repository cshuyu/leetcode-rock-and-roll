# Last updated: 4/16/2026, 3:49:20 PM
# Sliding window with fixed size
1class Solution:
2    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
3        left = right = 0
4        nums_set = set()
5        while right<len(nums):
6            if nums[right] in nums_set:
7                return True
8            else:
9                nums_set.add(nums[right])
10            right += 1
11            if right-left>k:
12                nums_set.remove(nums[left])
13                left += 1
14        return False
15