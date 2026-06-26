class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = dict()
        freq = dict()

        for num in nums:
            count[num] = count.get(num, 0) + 1
        
        # 1 : 2, 2 : 3
        
        for key in count:
            if count[key] not in freq:
                freq[count[key]] = []
                freq[count[key]].append(key)
            else:
                freq[count[key]].append(key)    

        ans = []

        for key in reversed(sorted(freq.keys())):
            for num in freq[key]:
                ans.append(num)
                if len(ans) == k:
                    return ans                
