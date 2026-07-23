# Last updated: 7/23/2026, 3:54:27 PM
1"""
2O(Time): O(n)
3O(Space): O(n)
4"""
5class Solution:
6    def subarraySum(self, nums: List[int], k: int) -> int:
7        count = 0
8        sum_dict = defaultdict(int)
9        sum_dict[0] = 1
10        prefix_sum = 0
11        for i in range(1, len(nums)+1):
12            prefix_sum = prefix_sum+nums[i-1]
13            expected_sum = prefix_sum - k
14            count += sum_dict[expected_sum]
15            sum_dict[prefix_sum] += 1
16        return count
17