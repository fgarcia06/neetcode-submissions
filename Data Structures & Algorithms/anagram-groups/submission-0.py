class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        ourMap = {}

        for string in strs:
            sorted_word = "".join(sorted(string))
            if sorted_word not in ourMap:
                ourMap[sorted_word] = []
            ourMap[sorted_word].append(string)

        return list(ourMap.values())