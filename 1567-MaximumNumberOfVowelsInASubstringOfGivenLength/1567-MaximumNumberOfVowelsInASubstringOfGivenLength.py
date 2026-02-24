# Last updated: 2/23/2026, 6:44:35 PM
class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        length = len(s)
        count = 0
        max_count = 0
        vowel_lst = ['a', 'e', 'i', 'o', 'u']
		
        for i in range(k):
            if s[i] in vowel_lst:
                count += 1

        max_count = max(count, max_count)
        for i in range(k, length):
            if s[i] in vowel_lst:
                count += 1
            if s[i-k] in vowel_lst:
                count -= 1
            max_count = max(max_count, count)

        return max_count        