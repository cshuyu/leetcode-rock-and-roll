# Last updated: 2/23/2026, 6:46:12 PM
class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        ans = 0

        for i in range(n):
            even = self.helper(s, i, i+1, n)
            odd = self.helper(s, i-1, i+1, n)
            ans += even+odd+1
        return ans

    def helper(self, s, i, j, n):
        cnt = 0
        while(i>=0 and j<n and s[i]==s[j]):
            cnt += 1
            i -= 1
            j += 1
        return cnt
        