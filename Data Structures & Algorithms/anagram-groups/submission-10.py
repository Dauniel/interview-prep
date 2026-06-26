class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = []
        anagrams = dict()
        for s in strs:
            sortedString = "".join(sorted(s))
            if sortedString not in anagrams:
                anagrams[sortedString] = []
                anagrams[sortedString].append(s)
            else:
                anagrams[sortedString].append(s)
        print(anagrams)
        for anagram in anagrams:
            ans.append(anagrams[anagram])
        return ans
