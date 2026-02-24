# Last updated: 2/23/2026, 6:45:59 PM
class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        free = 0
        hold = -prices[0]
        for i in range(1, len(prices)):
            prev_free = free
            prev_hold = hold
            free = max(prev_free, prev_hold+prices[i]-fee)
            hold = max(prev_hold, prev_free-prices[i])
        
        return free