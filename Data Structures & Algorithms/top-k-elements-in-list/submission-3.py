class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = dict() # value to count
        freq = dict() # count to list of values

        for num in nums:
            count[num] = count.get(num, 0) + 1
        
        for key, value in count.items():
            if value not in freq:
                freq[value] = []
                freq[value].append(key)
            else:
                freq[value].append(key)

        ans = []

        for key in reversed(sorted(freq.keys())):
            for num in freq[key]:
                ans.append(num)
                if len(ans) == k:
                    return ans
                    
