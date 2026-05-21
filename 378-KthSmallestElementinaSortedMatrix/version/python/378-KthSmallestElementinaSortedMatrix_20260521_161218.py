# Last updated: 5/21/2026, 4:12:18 PM
# Heap
1'''
2Time: O(nlogn+klogn)
3Space: O(n)
4'''
5class Solution:
6    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
7        minHeap = []
8        count = 0
9        for i in range(len(matrix)):
10            heapq.heappush(minHeap, (matrix[i][0], i, 0))
11        while count<k-1:
12            val, row, col = heapq.heappop(minHeap)
13            if col+1 < len(matrix[0]):
14                heapq.heappush(minHeap, (matrix[row][col+1], row, col+1))
15            count += 1
16        return minHeap[0][0]
17
18