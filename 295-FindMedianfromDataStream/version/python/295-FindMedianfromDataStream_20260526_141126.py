# Last updated: 5/26/2026, 2:11:26 PM
1'''
2addNum time Complexity: O(logn)
3Space Complexity: O(n)
4'''
5class MedianFinder:
6    def __init__(self):
7        self.maxHeap = []
8        self.minHeap = []
9
10    def addNum(self, num: int) -> None:
11        heapq.heappush(self.maxHeap, (-1)*num)
12        max_number = (-1)*heapq.heappop(self.maxHeap)
13        heapq.heappush(self.minHeap, max_number)
14        if len(self.minHeap)>len(self.maxHeap):
15            min_number = heapq.heappop(self.minHeap)
16            heapq.heappush(self.maxHeap, (-1)*min_number)
17
18    def findMedian(self) -> float:
19        max_number = (-1)*self.maxHeap[0]
20        if len(self.maxHeap)>len(self.minHeap):
21            return max_number
22        else:
23            min_number = self.minHeap[0]
24            return (max_number+min_number)/2
25
26        
27
28
29# Your MedianFinder object will be instantiated and called as such:
30# obj = MedianFinder()
31# obj.addNum(num)
32# param_2 = obj.findMedian()