# 1.Brute Force Approch
# Time Complexity is O(n^2)
class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        maxlen = 0
        for i in range(len(nums)):
            zeros = 0
            for j in range(i, len(nums)):
                if nums[j] == 0:
                    zeros += 1
                elif zeros <= k:
                    length = j - i + 1
                    maxlen = max(maxlen, length)
                else:
                    break
        return maxlen
# 2.Better Approches
# Time Complexity is O(2n)
class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left, right, maxlen, zeros = 0,0,0,0
        n = len(nums)
        while right < n:
            if nums[right] == 0:
                zeros += 1
            while zeros > k:
                if nums[left] == 0:
                    zeros -= 1
                left += 1
            if zeros <= k:
                length = right - left + 1
                maxlen = max(maxlen, length)
            right += 1
        return maxlen
# 3.Optimal Approches
# Time Complexity is O(n)
class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left, right, maxlen, zeros = 0,0,0,0
        n = len(nums)
        while right < n:
            if nums[right] == 0:
                zeros += 1
            if zeros > k:
                if nums[left] == 0:
                    zeros -= 1
                left += 1
            if zeros <= k:
                length = right - left + 1
                maxlen = max(maxlen, length)
            right += 1
        return maxlen
        