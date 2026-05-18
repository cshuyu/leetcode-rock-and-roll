# Last updated: 5/18/2026, 1:00:03 PM
# Heap with tuple
1'''
2Time Complexity: O(nlogn)
3we limit the heap size to be k, which can improve the complexity to nlogk
4Space Complexity: O(n)
5'''
6class Solution:
7    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
8        freqMap = defaultdict(int)
9        minHeap = []
10        res = []
11
12        for num in nums:
13            freqMap[num] += 1
14
15        for key in freqMap:
16            heapq.heappush(minHeap, (freqMap[key], key))
17            while len(minHeap) > k:
18                heapq.heappop(minHeap)
19        
20        for _,key in minHeap:
21            res.append(key)
22
23        return res
24