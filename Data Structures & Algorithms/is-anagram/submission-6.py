class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        checkS = dict()
        checkT = dict()

        for c in s:
            checkS[c] = checkS.get(c, 0) + 1
        for c in t:
            checkT[c] = checkT.get(c, 0) + 1
        
        return checkS == checkT
        
