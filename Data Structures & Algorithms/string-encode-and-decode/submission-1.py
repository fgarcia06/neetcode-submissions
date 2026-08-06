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
            # Find the delimiter
            j = i

            while s[j] != "#":
                j += 1

            # get the length  [i,j)
            length = int(s[i:j])

            # start of the string
            start = j + 1
            result.append(s[start:start + length])
            i = start + length

        return result