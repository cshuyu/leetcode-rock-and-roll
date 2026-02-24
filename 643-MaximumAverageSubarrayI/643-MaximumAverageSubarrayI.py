# Last updated: 2/23/2026, 6:46:13 PM
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        sum = 0
        for i in range(k):
            sum += nums[i]
        
        curr = sum
        for i in range(k, len(nums)):
            sum = sum + nums[i]-nums[i-k]
            curr = max(curr, sum)
        
        ans = curr/k
        return ans