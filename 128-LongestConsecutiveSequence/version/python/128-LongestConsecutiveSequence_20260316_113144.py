# Last updated: 3/16/2026, 11:31:44 AM
1class Solution:
2    def longestConsecutive(self, nums: List[int]) -> int:
3        # time complexity: O(n)
4        # space complexity: O(n)
5        num_set = set()
6        for num in nums:
7            num_set.add(num)
8        max_count = 0
9        for element in num_set:
10            count = 1
11            if element-1 in num_set:
12                continue
13            while element+1 in num_set:
14                element = element+1
15                count += 1
16            max_count = max(max_count, count)
17        return max_count
18