class Solution:
    def isValid(self, s: str) -> bool:
        check = {
            ")" : "(",
            "}" : "{",
            "]" : "["
        }
        stack = []
        for c in s:
            if c not in check:
                stack.append(c)
                continue
            else:
                if not stack or stack[-1] != check[c]:
                    return False
                stack.pop()
        return not stack