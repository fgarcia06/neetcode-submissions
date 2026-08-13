class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        midpoint = len(nums) // 2
        right = len(nums)

        while left < right:

            if target < nums[midpoint]:
                right = midpoint

            elif target > nums[midpoint]:
                left = midpoint + 1

            # midpoint is the target
            else:
                return midpoint
            
            midpoint = (left + right) // 2
        
        return -1

