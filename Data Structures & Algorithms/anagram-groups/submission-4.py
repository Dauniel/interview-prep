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
        
        # now we have a dictionary that contains a key (sortedword) and value being an array that contains all the words that correspond to that sorted word

        res = []

        for anagram in anagrams:
            res.append(anagrams[anagram])

        return res