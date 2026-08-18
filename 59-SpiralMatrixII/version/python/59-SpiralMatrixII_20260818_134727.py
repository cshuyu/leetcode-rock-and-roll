# Last updated: 8/18/2026, 1:47:27 PM
# Monotonic Queue
1"""
2O(Time): O(n)
3O(Space): O(n)
4"""
5class Solution:
6    def shortestSubarray(self, nums: List[int], k: int) -> int:
7        mq = deque([(-1, 0)])
8        prefix_sum = 0
9        min_length = float("inf")
10        for i in range(len(nums)):
11            prefix_sum += nums[i]
12            # keep the monotonic character
13            while mq and prefix_sum<=mq[-1][1]:
14                mq.pop()
15            mq.append((i, prefix_sum))
16            while mq and prefix_sum - mq[0][1]>=k:
17                min_length = min(min_length, i-mq[0][0])
18                mq.popleft()
19        if min_length == float("inf"):
20            return -1
21        else:
22            return min_length
23
24                    
25
26