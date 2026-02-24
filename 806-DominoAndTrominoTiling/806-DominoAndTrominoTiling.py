# Last updated: 2/23/2026, 6:45:12 PM
class Solution:
    def numTilings(self, n: int) -> int:
        if n<3:
            return n
        mod = 1000000007
        wholeTile = [0]*(n+1)
        partialTile = [0]*(n+1)
        wholeTile[1] = 1
        wholeTile[2] = 2
        partialTile[1] = 0
        partialTile[2] = 1
        for i in range(3, n+1):
            partialTile[i] = (partialTile[i-1]+wholeTile[i-2]) % mod
            wholeTile[i] = (wholeTile[i-1]+wholeTile[i-2]+2*partialTile[i-1]) % mod
        return wholeTile[n]
