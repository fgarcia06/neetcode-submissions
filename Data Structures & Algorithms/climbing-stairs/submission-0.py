class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 2

        ways_two_back = 1   # ways to reach the step two below current
        ways_one_back = 2   # ways to reach the step one below current

        for step in range(3, n + 1):
            current = ways_one_back + ways_two_back
            ways_two_back = ways_one_back
            ways_one_back = current

        return ways_one_back
        