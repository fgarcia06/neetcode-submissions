class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        storage = {}
        results = []

        for i in range(len(nums)):
            second = target - nums[i]

            if second not in storage:
                storage[nums[i]] = i
            else:
                results.append(storage.get(second))
                results.append(i)
        
        return results