class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        outputArray = [1] * len(nums)

        if nums is None:
            return 0

        # calculate the products on the left of the index
        prefix = 1

        for i in range(len(nums)):
            outputArray[i] = prefix
            prefix *= nums[i]

        # calculate the products on the right of the index
        suffix = 1

        for i in range(len(nums)-1, -1,-1):
            outputArray[i] *= suffix
            suffix *= nums[i]

        return outputArray
            