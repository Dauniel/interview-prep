class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = dict()
        frequencies = dict()
        for num in nums:
            count[num] = count.get(num, 0) + 1
        for key, value in count.items():
            if value not in frequencies:
                frequencies[value] = [key]
                #frequencies[value].append(key)
            else:
                frequencies[value].append(key)
        ans = []
        for key in reversed(sorted(frequencies.keys())):
            for num in frequencies[key]:
                ans.append(num)
                if len(ans) == k:
                    return ans