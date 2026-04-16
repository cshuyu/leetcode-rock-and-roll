# Last updated: 4/16/2026, 12:28:17 PM
# sliding window
1class Solution:
2    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
3        left = right = 0
4        product = 1
5        count = 0
6        if k<1:
7            return 0
8        while right<len(nums):
9           product = product*nums[right]
10           right += 1
11           while product>=k and left<right:
12            product = product/nums[left]
13            left += 1
14           if product<k:
15            # Every element between left and right forms a valid subarray 
16            # ending at 'right'
17            count += right-left
18        return count         
19            
20
21
22
23