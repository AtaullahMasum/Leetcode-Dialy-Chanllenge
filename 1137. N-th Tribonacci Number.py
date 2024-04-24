# Using Memoization
# Time Complexity is O(n)
# Space Complexity is O(n)
class Solution:
    def __init__(self):
        self.memo ={}
    def tribonacci(self, n: int) -> int:
        if n in self.memo:
            return self.memo[n]
        if n == 0:
            return 0
        if n == 1 or n == 2:
            return 1
        result = self.tribonacci(n-3) + self.tribonacci(n-2) + self.tribonacci(n-1)
        self.memo[n] = result
        return result
# Solution 2
class Solution:
    def tribonacci(self, n: int) -> int:
        if n==0:
            return 0
        if n== 1 or n == 2:
            return 1
        dp = [0]*(n+1)
        dp[0] = 0
        dp[1] = 1
        dp[2] = 1
        for i in range(3, n+1):
            dp[i] = dp[i-3] + dp[i-2] + dp[i-1]
        return dp[n]
        