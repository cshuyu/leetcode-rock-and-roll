# Last updated: 7/8/2026, 5:34:17 PM
1'''
2Time: O(n)
3Space: O(n)
4'''
5class Solution:
6    def twoSum(self, nums: List[int], target: int) -> List[int]:
7        remain_dict = defaultdict(int)
8        for i in range(len(nums)):
9            curr_num = nums[i]
10            if curr_num in remain_dict:
11                idx = remain_dict[curr_num]
12                return [i, idx]         
13            remain = target-nums[i]
14            remain_dict[remain] = i
15        return []
16