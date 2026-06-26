class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        ans = []
        anagrams = dict()
        for s in strs:
            sortedString = "".join(sorted(s))
            if sortedString not in anagrams:
                anagrams[sortedString] = [s]
            else:
                anagrams[sortedString].append(s)
        for anagram in anagrams:
            ans.append(anagrams[anagram])
        return ans
