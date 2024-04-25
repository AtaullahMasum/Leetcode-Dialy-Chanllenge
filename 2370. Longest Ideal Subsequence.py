# Brute Force Solution 
# Time Complexity is O(2^n)
# Space Complexity is O(n)
class Solution:
    def longestIdealString(self, s: str, k: int) -> int:
        cache = {}
        def helper (i, prev):
            if i == len(s):
                return 0
            res = helper(i+1, prev)  # skip
            if prev == "" or abs(ord(s[i]) - ord(prev)) <= k:
                res = max(res, 1+ helper(i+1, s[i])) # include
            return res
        return helper(0, "")
# Better Approch
# Time Complexity is O(n)
# Space Complexity is O(n^2 + n) 
#The memoization cache can store at most n^2 entries, 
#as each entry (i, prev) corresponds to a unique combination of indices and characters.
#Therefore, the space complexity for memoization is (n^2+n)
class Solution:
    def longestIdealString(self, s: str, k: int) -> int:
        cache = {}
        def helper (i, prev):
            if i == len(s):
                return 0
            if (i, prev) in  cache:
                return cache[(i, prev)]
            res = helper(i+1, prev) 
            if prev == "" or abs(ord(s[i]) - ord(prev)) <= k:
                res = max(res, 1+ helper(i+1, s[i]))
            cache[(i, prev)] = res
            return res
        return helper(0, "")
# Optimal SOlution Using Dynamic Programming
# Time Complexity is O(n*26) = O(n)
# Space Complexity is O(26) = O(1)
class Solution:
    def longestIdealString(self, s: str, k: int) -> int:
        dp = [0]*26
        for char in s:
            curr = ord(char) - ord('a')
            longest = 1
            for prev in range(26):
                if abs(curr - prev) <= k:
                    longest = max(longest, 1 + dp[prev])
            dp[curr] = longest
        return max(dp)
       

        