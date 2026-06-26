class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = dict()
        freq = dict()

        for num in nums:
            count[num] = count.get(num, 0) + 1 
        
        for number, frequency in count.items():
            if frequency not in freq:
                freq[frequency] = []
                freq[frequency].append(number)
            else:
                freq[frequency].append(number)
        
        ans = []

        for key in reversed(sorted(freq.keys())):
            for num in freq[key]:
                ans.append(num)
                if len(ans) == k:
                    return ans
