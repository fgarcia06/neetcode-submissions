class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dupe = {}

        for num in nums:
            if num not in dupe:
                dupe[num] = num
            else:
                return True
        return False