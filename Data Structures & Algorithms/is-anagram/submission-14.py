class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
    
        storage = {}

        for i in s:
            if i not in storage:
                storage[i] = 1
            else:
                storage[i] +=1
        
        for j in t:
            if j in storage and storage[j] > 0:
                storage[j] -=1
            else:
                return False
        
        return True