# Last updated: 7/21/2026, 6:07:14 PM
# Monotonic Queue
1"""
2O(Time): O(n)
3O(Space: O(n)
4"""
5class Solution:
6    def maxSubarraySumCircular(self, nums: List[int]) -> int:
7        n = len(nums)
8        prefix = [0]*(2*n+1)
9        for i in range(1, 2*n+1):
10            prefix[i] = prefix[i-1] + nums[(i-1)%n]
11
12        max_sum = float("-inf")
13        # small -> big
14        q = deque([0])
15        for i in range(1, 2*n+1):
16            while q and i-q[0]>n:
17                q.popleft()
18            if q:
19                max_sum = max(max_sum, prefix[i]-prefix[q[0]])
20            while q and prefix[q[-1]]>prefix[i]:
21                q.pop()
22            q.append(i)
23
24        return max_sum   