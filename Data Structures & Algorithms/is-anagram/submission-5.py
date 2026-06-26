class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        checkS = dict()
        checkT = dict()

        # Count characters in string s
        for c in s:
            checkS[c] = checkS.get(c, 0) + 1
        
        # Count characters in string t
        for c in t:
            checkT[c] = checkT.get(c, 0) + 1
        
        # Compare dictionaries
        if len(checkS) != len(checkT):
            return False
        
        for key in checkS:
            if checkS[key] != checkT.get(key, 0):
                return False
        
        return True
