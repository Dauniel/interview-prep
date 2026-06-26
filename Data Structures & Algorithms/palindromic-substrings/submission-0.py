class Solution:
    def countSubstrings(self, s: str) -> int:
        palindromes = []
        for i in range(len(s)):
            for j in range(i + 1, len(s) + 1):
                substring = s[i:j]
                if self.ispalindrome(substring):
                    palindromes.append(substring)
        print(palindromes)
        return len(palindromes)
    def ispalindrome(self, s: str) -> bool:
        if s == s[::-1]:
            return True
        return False
    
