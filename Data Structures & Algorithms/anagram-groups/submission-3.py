class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = dict()

        for s in strs:
            sortedWord = "".join(sorted(s))
            if sortedWord not in anagrams:
                anagrams[sortedWord] = []
                anagrams[sortedWord].append(s)
            else:
                anagrams[sortedWord].append(s)
        
        ans = []

        for anagram in anagrams:
            ans.append(anagrams[anagram])

        return ans