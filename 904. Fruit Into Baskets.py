# Brute Force Approch
# Time Complexity O(n^2)
# This Solution is Time Limit Exceeds
class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        maxlen = 0
        for i in range(len(fruits)):
            hashSet = set()
            for j in range(i, len(fruits)):
                hashSet.add(fruits[j])
                if len(hashSet) <= 2:
                    maxlen = max(maxlen, j - i + 1)
                else:
                    break
        return maxlen
