# Last updated: 2/23/2026, 6:46:05 PM
class Solution:
    def isPalindrome(self, s, first, last, allowed_mismatch) -> bool:
        if not s:
            return False
        while first < last:
            if s[first] != s[last]:
                if allowed_mismatch == 0:
                    return False
                if self.isPalindrome(s, first+1, last, allowed_mismatch-1):
                    return True
                if self.isPalindrome(s, first, last-1, allowed_mismatch-1):
                    return True
                return False
            first += 1
            last -= 1
        return True
        
    def validPalindrome(self, s: str) -> bool:
        return self.isPalindrome(s, 0, len(s)-1, 1)
        