class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lowest = prices[0]
        maxProfit = 0
        for price in prices:
            maxProfit = max(maxProfit, price - lowest)
            lowest = min(lowest, price)
        return maxProfit