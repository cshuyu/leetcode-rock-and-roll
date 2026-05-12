# Last updated: 5/11/2026, 5:10:36 PM
# Sliding window: 2nd try
1class Solution:
2    def minOperations(self, nums: List[int], x: int) -> int:
3        nums_length = len(nums)
4        total = 0
5        for num in nums:
6            total += num
7        target = total - x
8        left = right = 0
9        max_length = -1
10        curr_sum = 0
11        while right<nums_length:
12            curr_sum += nums[right]
13            while curr_sum > target and left<=right:
14                # shrink the left
15                curr_sum -= nums[left]
16                left += 1
17            if curr_sum == target:
18                max_length = max(max_length, right-left+1)
19            right += 1
20        
21        if max_length == -1:
22            return -1
23        else:
24            return nums_length-max_length
25
26            
27