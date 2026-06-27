class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        flag = False
        dupe = list(t)
        if len(s) != len(t):
            flag = False
            return flag

        for i in s:
            if i in dupe:
                flag = True
                dupe.remove(i)
            else:
                flag = False
                return flag
        return flag
        