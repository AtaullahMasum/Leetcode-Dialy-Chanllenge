# Optimal Solution Using Dynamic Programming
# Time Complexity is O(n^2)
# Space Complexity is O(n^2)
class Solution:
    def minFallingPathSum(self, arr: List[List[int]]) -> int:
        rows = len(arr)
        cols = len(arr[0])
        
        # Initialize dp array to store the minimum falling path sum
        dp = [[0] * cols for _ in range(rows)]
        
        # Copy the first row from the input array to the dp array
        for j in range(cols):
            dp[0][j] = arr[0][j]
        
        # Iterate over the remaining rows and update dp array
        for i in range(1, rows):
            # Find the two minimum values in the previous row
            min1, min2 = float('inf'), float('inf')
            for j in range(cols):
                if dp[i-1][j] < min1:
                    min2 = min1
                    min1 = dp[i-1][j]
                elif dp[i-1][j] < min2:
                    min2 = dp[i-1][j]
            
            # Update dp array with the minimum falling path sum
            for j in range(cols):
                if dp[i-1][j] == min1:
                    dp[i][j] = min2 + arr[i][j]
                else:
                    dp[i][j] = min1 + arr[i][j]
        
        # Find the minimum falling path sum in the last row
        return min(dp[-1])
