class Solution:
    def combinationSum(self, nums, target):
        res = []

        def dfs(start, path, total):
            if total == target:
                res.append(path)
                return
            if total > target:
                return

            for i in range(start, len(nums)):
                dfs(i, path + [nums[i]], total + nums[i])

        dfs(0, [], 0)
        return res
