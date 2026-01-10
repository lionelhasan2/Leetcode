class Solution:
    def climbStairs(self, n: int) -> int:

        cache = [-1]* (n)
        def dfs(i):
            # Base case, a path to the target number has been found, return 1 to signal
            if i==n:
                return 1
            # Base case, we have passed the target number just return 0
            if i>n:
                return 0
            if cache[i] != -1:
                return cache[i]
            # At each step we can go either 1 or 2 steps
            cache[i] = dfs(i+1) + dfs(i+2)
            return cache[i]
        return dfs(0)
                