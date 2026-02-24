# Last updated: 2/23/2026, 6:45:00 PM
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def canFinish(k: int) -> boolean:
            hours = 0
            for pile in piles:
                hours += pile//k
                if pile%k != 0:
                    hours += 1
                if hours > h:
                    return False
            return True

        left = 1
        right = max(piles)
        while left<right:
            mid = int(left + (right-left)/2)
            if canFinish(mid):
                right = mid
            else:
                left = mid+1
        return left