class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        check = dict()
        ans = 0
        left = 0
        maxC = 0
        for right in range(len(s)):
            check[s[right]] = check.get(s[right], 0) + 1
            maxC = max(maxC, check[s[right]])
            if (right - left + 1) - maxC > k:
                check[s[left]] -= 1
                left += 1
            ans = max(ans, right - left + 1)
        return ans
                