# Last updated: 2/23/2026, 6:46:22 PM
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        sums = {0: 1}
        s = 0
        cnt = 0
        for i in range(len(nums)):
            s += nums[i]
            diff = s - k
            cnt += sums.get(diff, 0)
            sums[s] = sums.get(s,0) + 1
        return cnt
        