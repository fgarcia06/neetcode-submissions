class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashMap = {}
        ind = []

        for i in range(0,len(nums)):
            if (target - nums[i]) in hashMap:
                ind.append(hashMap.get(target-nums[i]))
                ind.append(i)
            else:
                hashMap[nums[i]] = i
        return ind
