# Brute Force Approch
# Time Complexity is O(n^2)
class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        cnt = 0
        for i in range(len(s)):
            hashSet = set()
            for j in range(i, len(s)):
                hashSet.add(s[j])
                if len(hashSet) == 3:
                    cnt += 1
        return cnt
# Better than Brute force Approch
# But Also issues of Time Limit Exceed
class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        cnt = 0
        n = len(s)
        for i in range(n):
            hashSet = set()
            for j in range(i, n):
                hashSet.add(s[j])
                if len(hashSet) == 3:
                    cnt += (n-j)
                    break
        return cnt