class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        ourMap = {}

        for s in strs:
            count = [0] * 26

            for i in s:
                count[ord(i)-ord('a')] += 1

            if tuple(count) not in ourMap:
                ourMap[tuple(count)] = [s]
            else:
                ourMap[tuple(count)].append(s)
        return list(ourMap.values())