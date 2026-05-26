# Last updated: 5/26/2026, 2:04:08 PM
# Heap with divide&conquer
1class MedianFinder:
2
3    def __init__(self):
4        self.maxHeap = []
5        self.minHeap = []
6
7    def addNum(self, num: int) -> None:
8        heapq.heappush(self.maxHeap, (-1)*num)
9        max_number = (-1)*heapq.heappop(self.maxHeap)
10        heapq.heappush(self.minHeap, max_number)
11        if len(self.minHeap)>len(self.maxHeap):
12            min_number = heapq.heappop(self.minHeap)
13            heapq.heappush(self.maxHeap, (-1)*min_number)
14
15    def findMedian(self) -> float:
16        max_number = (-1)*self.maxHeap[0]
17        if len(self.maxHeap)>len(self.minHeap):
18            return max_number
19        else:
20            min_number = self.minHeap[0]
21            return (max_number+min_number)/2
22
23        
24
25
26# Your MedianFinder object will be instantiated and called as such:
27# obj = MedianFinder()
28# obj.addNum(num)
29# param_2 = obj.findMedian()