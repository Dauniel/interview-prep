class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        check = set()
        ans = 0 
        left = 0
        for right in range(len(s)):
            while s[right] in check:
                check.remove(s[left])
                left += 1
            ans = max(ans, right - left + 1)
            check.add(s[right])
        return ans