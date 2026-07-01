class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ourMap = {}
        output = []
        for num in nums:
            if num not in ourMap:
                ourMap[num] = 1
            else:
                ourMap[num] += 1
        
        while k:
            maxi = max(ourMap, key=ourMap.get)
            output.append(maxi)
            del ourMap[maxi]
            k -= 1
        return output
        


