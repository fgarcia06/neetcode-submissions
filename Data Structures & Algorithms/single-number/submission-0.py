class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        mp = {}

        for i in range(len(nums)):
            if nums[i] not in mp:
                mp[nums[i]] = 1
            else:
                mp[nums[i]] = 2
        
        for key, value in mp.items():
            if value == 1:
                return key
