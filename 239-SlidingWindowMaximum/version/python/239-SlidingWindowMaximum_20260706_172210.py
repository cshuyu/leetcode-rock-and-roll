# Last updated: 7/6/2026, 5:22:10 PM
1"""
2heap
3time: O(n*logk)
4space: O(n)
5"""
6class Solution:
7    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
8        pq = []
9        res = []
10        for idx in range(len(nums)):
11            heapq.heappush(pq, (-nums[idx], idx))
12            while pq and pq[0][1]<=idx-k:
13                heapq.heappop(pq)
14            
15            if idx>=k-1:
16                res.append(-pq[0][0])
17        return res
18