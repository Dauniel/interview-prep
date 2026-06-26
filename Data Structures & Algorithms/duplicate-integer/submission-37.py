class Solution:
    def hasDuplicate(self, nums: list[int]) -> bool:
        check = set()
        for num in nums:
            if num in check:
                return True 
            else:
                check.add(num)
        return False
