class Solution:
    def longestPalindrome(self, s: str) -> str:
        palindromes = []
        for i in range(len(s)):
            for j in range(i + 1, len(s) + 1):
                if s[i:j] == s[i:j][::-1]:
                    palindromes.append(s[i:j])
        longest = ""
        for s in palindromes:
            if len(s) > len(longest):
                longest = s
        return longest