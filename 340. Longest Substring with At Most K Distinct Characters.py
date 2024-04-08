# Brute Force Approch
# Time Complexity is O(n^2)
# Space Complexity is O(256)
class Solution:
    def longestKSubstr(self, s, k):
        # code here
        maxlen , hashMap = 0, {}
        for i in range(len(s)):
            hashMap.clear()
            for j in range(i, len(s)):
                hashMap[s[j]] = hashMap.get(s[j], 0) + 1
                if len(hashMap) <= k:
                    maxlen = max(maxlen, j-i+1)
                else:
                    break
        return maxlen
# Better Solution
# Time Complexity is O(n+n)
# Space Complexity is O(256)
class Solution:
    def longestKSubstr(self, s, k):
        # code here
        maxlen , hashMap = -1, {}
        left, right = 0, 0
        n = len(s)
        while right < n:
            hashMap [s[right]] = hashMap.get(s[right], 0) + 1
            if len(hashMap) > k:
                while len(hashMap) > k:
                    hashMap[s[left]] -= 1
                    if hashMap[s[left]] == 0:
                        hashMap.pop(s[left])
                    left += 1
            if len(hashMap) == k:
                maxlen = max(maxlen, right - left + 1)
            right += 1    
        return maxlen
# Optimal Solution Added 
# Time Complexity is O(n)
# Space Complexity is O(256)
class Solution:
    def longestKSubstr(self, s, k):
        # code here
        maxlen , hashMap = -1, {}
        left, right = 0, 0
        n = len(s)
        while right < n:
            hashMap [s[right]] = hashMap.get(s[right], 0) + 1
            if len(hashMap) > k:
                hashMap[s[left]] -= 1
                if hashMap[s[left]] == 0:
                    hashMap.pop(s[left])
                left += 1
            if len(hashMap) == k:
                maxlen = max(maxlen, right - left + 1)
            right += 1
        return maxlen

