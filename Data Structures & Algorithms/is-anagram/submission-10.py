class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        tDict = {}

        for i in t:
            if i not in tDict:
                tDict[i] = 1
            else:
                tDict[i] += 1
        
        for j in s:
            if j in tDict and tDict[j] > 0:
                tDict[j] -= 1
            else:
                return False
        return True