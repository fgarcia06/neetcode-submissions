class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dupe = {}

        for num in nums:
            if num not in dupe:
                dupe[num] = 1
            else:
                return True
        return False