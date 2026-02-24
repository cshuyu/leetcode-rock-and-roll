# Last updated: 2/23/2026, 6:44:39 PM
class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        for i, char in enumerate(s):
            if char == '(':
                stack.append(i)
            elif char == ')':
                if stack and s[stack[-1]] == '(':
                    stack.pop()
                else:
                    stack.append(i)
        
        result = []
        for i, char in enumerate(s):
            if stack and i == stack[0]:
                stack.pop(0)
                continue
            result.append(char)
        
        return ''.join(result)

