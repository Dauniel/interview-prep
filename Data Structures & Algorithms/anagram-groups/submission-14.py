class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        ans = []
        anagrams = dict()
        for s in strs:
            anagram = "".join(sorted(s))
            if anagram not in anagrams:
                anagrams[anagram] = [s]
            else:
                anagrams[anagram].append(s)
        for anagram in anagrams:
            ans.append(anagrams[anagram])
        
        return ans
        
