class Solution:
    def longestPalindrome(self, s: str) -> str:
        strs = []
        for i in range(len(s)):
            for j in range(i + 1, len(s) + 1):
                if s[i:j] == s[i:j][::-1]:
                    strs.append(s[i:j])
        ans = ""
        for s in strs:
            if len(s) > len(ans):
                ans = s
        return ans