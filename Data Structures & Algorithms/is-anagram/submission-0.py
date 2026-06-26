class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        checkS = dict()
        checkT = dict()
        
        for c in s:
            if c not in checkS:
                checkS[c] = 1
            else:
                checkS[c] += 1
        for c in t:
            if c not in checkT:
                checkT[c] = 1
            else:
                checkT[c] += 1
        return checkS == checkT
