# Last updated: 2/23/2026, 6:44:16 PM
class Solution:
    def removeStars(self, s: str) -> str:
        res = []
        for i in range(len(s)):
            if s[i] != "*":
                res.append(s[i])
            else:
                res.pop()
        return ''.join(res)



