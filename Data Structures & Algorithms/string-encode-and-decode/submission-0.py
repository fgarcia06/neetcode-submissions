class Solution:

    def encode(self, strs: List[str]) -> str:
        string_placeholder = []

        for string in strs:
            string_placeholder.append(str(len(string))+'#'+string)

        s = ''.join(string_placeholder)

        return s


    def decode(self, s: str) -> List[str]:
        result = []
        i = 0

        while i < len(s):
            j = i

            while s[j] != "#":
                j += 1

            length = int(s[i:j])
            start = j + 1
            result.append(s[start:start + length])
            i = start + length

        return result