class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        midpoint = len(nums) // 2
        right = len(nums)
        
        if target not in nums:
            return -1

        while left < right:

            if target < nums[midpoint]:
                right = midpoint
                midpoint = (left + right) // 2

            elif target > nums[midpoint]:
                left = midpoint
                midpoint = (left + right) // 2

            # midpoint is the target
            elif target == nums[midpoint]:
                return midpoint

