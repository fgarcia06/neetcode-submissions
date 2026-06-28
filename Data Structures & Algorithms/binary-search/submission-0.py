class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0 
        right = len(nums) - 1

        while left <= right:
            midpoint = (left+right) // 2

            if nums[midpoint] == target:
                return midpoint
            elif target < nums[midpoint]:
                right = midpoint - 1
            else:
                left = midpoint +  1
        return -1