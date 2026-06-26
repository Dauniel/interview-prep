class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False
        checkS = dict()
        checkT = dict()
        for i in range(len(s)):
            checkS[s[i]] = checkS.get(s[i], 1) + 1
            checkT[t[i]] = checkT.get(t[i], 1) + 1
        return checkS == checkT
            