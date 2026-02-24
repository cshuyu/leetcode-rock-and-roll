# Last updated: 2/23/2026, 6:44:33 PM
class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        left = 0
        zero_cnt = 0
        ans = 0
        for right in range(len(nums)):
            if nums[right] == 0:
                zero_cnt += 1
            while zero_cnt>1:
                if nums[left] == 0:
                    zero_cnt -= 1
                left += 1
            ans = max(ans, right-left)
        return ans

