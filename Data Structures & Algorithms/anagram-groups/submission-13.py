class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # list of strings
        check = dict()
        for s in strs:
            key = "".join(sorted(s))
            if key not in check:
                check[key] = [s]
            else:
                check[key].append(s)
        
        # now check has key value 
        # key -> sorted anagram 
        # value -> list of words corresponding to that anagram 
        ans = []
        for key, value in check.items():
            ans.append(value)
        return ans
