class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        else:
            checkS = dict()
            checkT = dict()
            for i in range(len(s)):
                s_char = s[i]
                t_char = t[i]
                checkS[s_char] = checkS.get(s_char, 0) + 1
                checkT[t_char] = checkT.get(t_char, 0) + 1
            for key in checkS:
                if key not in checkT:
                    return False
                elif checkS[key] != checkT[key]:
                    return False
            return True

