# Last updated: 7/7/2026, 12:21:39 AM
# priority queue
1class Solution:
2    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
3        num_freq = defaultdict(int)
4        pq = []
5        res = []
6        for num in nums:
7            num_freq[num] = num_freq[num]+1
8        
9        for val, count in num_freq.items():
10            heapq.heappush(pq, (count, val))
11            while len(pq)>k:
12                heapq.heappop(pq)
13        for element in pq:
14            res.append(element[1])
15        return res
16
17        
18        