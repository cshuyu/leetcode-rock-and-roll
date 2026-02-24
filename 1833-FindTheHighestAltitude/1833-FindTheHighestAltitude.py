# Last updated: 2/23/2026, 6:44:24 PM
class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        ans = 0
        curr = 0
        for i in range(len(gain)):
            curr += gain[i]
            ans = max(ans, curr)
        return ans