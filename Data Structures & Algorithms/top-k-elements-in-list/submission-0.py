class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = dict()
        freq = dict()
        for num in nums:
            count[num] = 1 + count.get(num, 0)

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
        
