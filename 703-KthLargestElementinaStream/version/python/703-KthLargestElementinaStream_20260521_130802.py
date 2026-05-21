# Last updated: 5/21/2026, 1:08:02 PM
# Heap
1'''
2Initialization: nlog(k)
3add: log(k)
4'''
5class KthLargest:
6    def __init__(self, k: int, nums: List[int]):
7        self.minHeap = []
8        self.k = k
9        for num in nums:
10            heapq.heappush(self.minHeap, num)
11            if len(self.minHeap)>self.k:
12                heapq.heappop(self.minHeap)
13
14    def add(self, val: int) -> int:
15        heapq.heappush(self.minHeap, val)
16        if len(self.minHeap) > self.k:
17            heapq.heappop(self.minHeap)
18        return self.minHeap[0]
19
20
21
22# Your KthLargest object will be instantiated and called as such:
23# obj = KthLargest(k, nums)
24# param_1 = obj.add(val)
25