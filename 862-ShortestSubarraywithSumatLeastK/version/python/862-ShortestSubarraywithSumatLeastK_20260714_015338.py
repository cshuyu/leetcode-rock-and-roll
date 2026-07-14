# Last updated: 7/14/2026, 1:53:38 AM
# Monotonic queue with prefix_sum
1"""
2prefix_sum + sliding_window + monotonic_queue
3O(Time): O(n)
4O(Space): O(n)
5"""
6class Solution:
7    def shortestSubarray(self, nums: List[int], k: int) -> int:
8        prefix_sum = 0
9        mq = deque([(-1, prefix_sum)])
10        min_length = float("inf")
11
12        for idx in range(len(nums)):
13            prefix_sum += nums[idx]
14            
15            while mq and prefix_sum < mq[-1][1]:
16                mq.pop()
17            mq.append((idx, prefix_sum))
18
19            while prefix_sum - mq[0][1]  >= k:
20                min_length = min((idx-mq[0][0]), min_length)
21                mq.popleft()
22        
23        if min_length == float("inf"):
24            return -1
25        else:
26            return min_length
27
28