class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dupe = {}
        for num in nums:
            if num in dupe:
                return True
                break
            dupe[num] = True
        return False
        