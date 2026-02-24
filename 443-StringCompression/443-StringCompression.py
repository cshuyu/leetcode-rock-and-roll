# Last updated: 2/23/2026, 6:47:19 PM
class Solution:
    def compress(self, chars: List[str]) -> int:
        length = len(chars)
        i = 0
        ans = 0
        
        while i<length:
            letter = chars[i]
            count = 0
            chars[ans] = letter
            ans += 1
            while i<length and chars[i]==letter:
                count += 1
                i += 1
            if count>1:
                for c in str(count):
                    chars[ans] = c
                    ans += 1
        
        return ans

        