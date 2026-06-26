class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        anagrams = dict()
        ans = []
        for s in strs:
            sortedString = "".join(sorted(s))
            if sortedString not in anagrams:
                anagrams[sortedString] = [s]
            else:
                anagrams[sortedString].append(s)
        print(anagrams)
        for anagram in anagrams:
            ans.append(anagrams[anagram])
        return ans
