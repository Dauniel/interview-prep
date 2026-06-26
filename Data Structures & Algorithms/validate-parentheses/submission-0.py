class Solution:
    def isValid(self, s: str) -> bool:
        key = {
            ')' : '(',
            ']' : '[',
            '}' : '{'
        }
        stack = []
        for c in s:
            if c not in key:
                stack.append(c)
                continue
            elif not stack or stack[-1] != key[c]:
                return False
            stack.pop()
        return not stack