class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        check = dict()

        for i in range(len(nums)):
            if target - nums[i] in check:
                return [check[target - nums[i]], i]
            else:
                check[nums[i]] = i # key is the element itself, value is the index corresponding to that element