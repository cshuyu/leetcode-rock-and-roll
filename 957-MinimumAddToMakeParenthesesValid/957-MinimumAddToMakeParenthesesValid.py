# Last updated: 2/23/2026, 6:44:56 PM
class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        if not s:
            return 0
        stack = []
        ending_cnt = 0
        for char in s:
            if char == ")":
                if not stack:
                    ending_cnt +=1
                else:
                    stack.pop()
            else:
                stack.append(char)
        return ending_cnt + len(stack)

