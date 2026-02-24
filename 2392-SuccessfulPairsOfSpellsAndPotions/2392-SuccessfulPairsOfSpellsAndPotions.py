# Last updated: 2/23/2026, 6:44:19 PM
class Solution:
    def findlargestFailureIdx(self, i, j, spell, potions, success):
            findIdx = -1
            while i<=j:
                mid = int(i+(j-i)/2)
                if spell*potions[mid]<success:
                    findIdx = mid
                    i = mid+1
                else:
                    j = mid-1
            return findIdx

    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions.sort()
        res = []
        for spell in spells:
            i = 0
            j = len(potions)-1
            idx = self.findlargestFailureIdx(i, j, spell, potions, success)
            res.append(j-idx)
        return res
