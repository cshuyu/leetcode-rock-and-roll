# Last updated: 5/18/2026, 11:30:45 AM
# Heap
1class Solution:
2    def findKthLargest(self, nums: List[int], k: int) -> int:
3        maxHeap = []
4        for num in nums:
5            heapq.heappush(maxHeap, (-1)*num)
6        while k>0:
7            curr_max = (-1)*heapq.heappop(maxHeap)
8            k -= 1
9            if k==0:
10                return curr_max
11      