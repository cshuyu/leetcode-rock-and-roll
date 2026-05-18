# Last updated: 5/18/2026, 3:01:12 PM
# bucket sort
1'''
2Time Complexity: O(n)
3Space Complexity: O(n)
4'''
5class Solution:
6    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
7        freqMap = defaultdict(int)
8        buckets = [[] for i in range(len(nums)+1)]
9        res = []
10
11        for num in nums:
12            freqMap[num] += 1
13
14        for key in freqMap:
15            buckets[freqMap[key]].append(key)
16        
17        for i in range(len(buckets)-1, 0, -1):
18            for num in buckets[i]:
19                res.append(num)
20                if len(res) == k:
21                    return res