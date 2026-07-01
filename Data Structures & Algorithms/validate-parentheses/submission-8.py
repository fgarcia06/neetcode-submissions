class Solution:
    def isValid(self, s: str) -> bool:
        mapping ={
            ")": "(",
            "]": "[",
            "}": "{"
        }

        stack = []

        for paren in s:
            if paren in mapping.values():
                stack.append(paren)

            elif (paren in mapping):
                if len(stack) == 0:
                    return False
                if mapping[paren] != stack[-1]:
                    return False
                stack.pop()

            else:
                return False

        return len(stack) == 0