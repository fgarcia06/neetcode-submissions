class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        results = [0] * len(temperatures)
        stack = []

        stack.insert(0, 0)

        for i in range(1, len(temperatures)):

            while stack and temperatures[stack[-1]] < temperatures[i]:
                results[stack[-1]] = i - stack[-1]
                stack.pop()
            stack.append(i)

        return results

