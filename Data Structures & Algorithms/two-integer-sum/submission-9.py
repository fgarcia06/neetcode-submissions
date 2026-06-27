class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashMap = {}
        ind = []

        for i in range(0,len(nums)):
            complement = target - nums[i]
            if (complement) in hashMap:
                return [hashMap.get(complement),i]
            else:
                hashMap[nums[i]] = i
