# Last updated: 2/23/2026, 6:44:53 PM
class Solution(object):
    def maxWidthRamp(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        maxRight = [0]*n
        preMax = -1
        
        for i in range(n-1, -1, -1):
            maxRight[i] = max(nums[i], preMax)
            preMax = maxRight[i]
        print(maxRight)
        res = 0
        l = 0
        for r in range(n):
            while nums[l]>maxRight[r]:
                l = l+1
            res = max(res, r-l)
        return res