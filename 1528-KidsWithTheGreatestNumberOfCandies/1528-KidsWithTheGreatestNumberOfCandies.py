# Last updated: 2/23/2026, 6:44:37 PM
class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        largest = max(candies)
        res = []
        for candy in candies:
            if candy + extraCandies >= largest:
                res.append(True)
            else:
                res.append(False)
        return res
            

