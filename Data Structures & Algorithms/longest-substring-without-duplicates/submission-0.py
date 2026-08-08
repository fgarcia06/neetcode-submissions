class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hashMap = {}
        start = 0
        length = 0

        for i in range(len(s)):
            # shrink the window
            while hashMap.get(s[i], 0) > 0:
                hashMap[s[start]] -= 1
                start += 1 # increment left

            # add current char to window
            hashMap[s[i]] = hashMap.get(s[i], 0) + 1

            # get current valid length
            current_length = i - start + 1

            length = max(length, current_length)

        return length
    
            
            

                