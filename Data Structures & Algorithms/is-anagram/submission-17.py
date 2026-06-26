class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        checkS = dict()
        checkT = dict()

        length = len(s)

        for i in range(length):
            checkS[s[i]] = checkS.get(s[i], 0) + 1
            checkT[t[i]] = checkT.get(t[i], 0) + 1

        return checkS == checkT        