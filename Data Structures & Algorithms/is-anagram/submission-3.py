class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        array = list(s)
        for letter in t:
            if letter in array and len(s) == len (t):
                array.remove(letter)
            else:
                return False
                break
        return True