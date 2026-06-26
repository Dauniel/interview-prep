class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = set()
        ans = 0
        left = 0

        for right in range(len(s)):
            while s[right] in charSet:
                charSet.remove(s[left])
                left += 1
            charSet.add(s[right])
            ans = max(ans, len(charSet))
        return ans

            
