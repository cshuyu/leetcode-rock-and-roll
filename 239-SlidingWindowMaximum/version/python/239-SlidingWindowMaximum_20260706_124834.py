# Last updated: 7/6/2026, 12:48:34 PM
1"""
2sliding window + monotonic queue
3time: O(n)
4space: O(n)
5"""
6class Solution:
7    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
8        dq = deque()
9        res = []
10        left=right=0
11        while right<len(nums):
12            while dq and nums[dq[-1]]<nums[right]:
13                dq.pop()
14            dq.append(right)
15            right += 1
16
17            while right-left>k:
18                if dq[0]<=left:
19                    dq.popleft()
20                left += 1
21            
22            if right-left==k:
23                res.append(nums[dq[0]])
24        return res
25
26
27
28
29
30
31