class Solution:
    def longestPalindrome(self, s: str) -> str:
        palindromes = []
        for i in range(len(s)):
            for j in range(i + 1, len(s) + 1):
                substring = s[i:j]
                if substring == substring[::-1]:
                    palindromes.append(substring)
        
        # Correct lambda usage

        longest_string = max(palindromes, key=len)

        return longest_string
