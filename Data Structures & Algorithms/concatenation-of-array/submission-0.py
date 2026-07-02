class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        dupe = nums
        ans = dupe + nums
        return ans