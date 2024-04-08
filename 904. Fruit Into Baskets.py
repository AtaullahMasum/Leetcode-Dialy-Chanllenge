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
# Better solution Added
# Time Complexity is O(N+N)
# Space Complexity is O(3)
class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        left, right , maxlen  = 0, 0, 0
        hashMap = {}
        n = len(fruits)
        while right < n:
            # Update frequency of fruit at index 'right'
            hashMap[fruits[right]]  = hashMap.get(fruits[right], 0) + 1 
            # Check if there are more than 2 types of fruits
            if len(hashMap) > 2:
                while len(hashMap) > 2:
                    hashMap[fruits[left]] -= 1
                    # Move 'left' pointer to remove one type of fruit
                    if hashMap[fruits[left]] == 0:
                        hashMap.pop(fruits[left])
                    left += 1
            # Update maxlen
            if len(hashMap) <= 2:
                maxlen = max(maxlen, right - left + 1)
            right += 1
        return maxlen
# Optimal Solution Added
# Time Complexity is O(n)
# Space Complexity is O(3)
class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        left, right , maxlen  = 0, 0, 0
        hashMap = {}
        n = len(fruits)
        while right < n:
            # Update frequency of fruit at index 'right'
            hashMap[fruits[right]]  = hashMap.get(fruits[right], 0) + 1 
            # Check if there are more than 2 types of fruits
            if len(hashMap) > 2: 
                hashMap[fruits[left]] -= 1
                # Move 'left' pointer to remove one type of fruit
                if hashMap[fruits[left]] == 0:
                    hashMap.pop(fruits[left])
                left += 1
            # Update maxlen
            if len(hashMap) <= 2:
                maxlen = max(maxlen, right - left + 1)
            right += 1
        return maxlen
                
                