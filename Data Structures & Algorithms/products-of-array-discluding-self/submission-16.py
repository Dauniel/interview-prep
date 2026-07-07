class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = []
        for _ in range(n):
            ans.append(1)
        
        prefix = 1
        for i in range(n):
            ans[i] = prefix
            prefix = prefix * nums[i]
        
        suffix = 1
        for i in range(n - 1, -1, -1):
            ans[i] = ans[i] * suffix
            suffix = suffix * nums[i]
        
        return ans