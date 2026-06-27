class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        extra = []
        for num in nums:
            if num in extra:
                return True
                break
            else:
                extra.append(num)
        return False
            