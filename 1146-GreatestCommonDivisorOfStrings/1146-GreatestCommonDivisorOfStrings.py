# Last updated: 2/23/2026, 6:44:45 PM
class Solution:
    def gcd(self, len1: int, len2: int) -> int:
        if len2 == 0:
            return len1
        return self.gcd(len2, len1 % len2)


    def gcdOfStrings(self, str1: str, str2: str) -> str:
        # gcdBase: m * len(gcdBase) == str1
        #.         n * len(gcdBase) == str2
        #          m and n is not divicible. 
        #          m1 * len(gcdBaseSmall)
        #          n1 * len(gcdBaseSmall)
        # elemA1 | elemA2 | elemA3 | elemB1 | elemB2
        # elemB1 | elemB2 | elemA1 | elemA2 | elemA3
        if str1 + str2 != str2 + str1:
            return ""
        g = self.gcd(len(str1), len(str2))
        return str1[:g]