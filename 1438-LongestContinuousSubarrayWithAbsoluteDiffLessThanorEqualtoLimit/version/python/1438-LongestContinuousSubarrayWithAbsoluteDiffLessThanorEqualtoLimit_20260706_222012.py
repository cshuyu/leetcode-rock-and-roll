# Last updated: 7/6/2026, 10:20:12 PM
# Monotonic Queue
1"""
2Sliding window + monotonic queue
3O(Time): O(n)
4O(Space): O(n)
5"""
6class Solution:
7    def longestSubarray(self, nums: List[int], limit: int) -> int:
8        min_dq = deque()
9        max_dq = deque()
10        left = 0
11        right = 0
12        max_length = 0
13        while right<len(nums):
14            while min_dq and nums[min_dq[-1]]>nums[right]:
15                min_dq.pop()
16            min_dq.append(right)
17            while max_dq and nums[max_dq[-1]]<nums[right]:
18                max_dq.pop()
19            max_dq.append(right)
20            right += 1
21            while nums[max_dq[0]]-nums[min_dq[0]]>limit:
22                if min_dq[0] == left:
23                    min_dq.popleft()
24                if max_dq[0] == left:
25                    max_dq.popleft()
26                left += 1
27            
28            max_length = max(max_length, right-left)
29        return max_length
30
31