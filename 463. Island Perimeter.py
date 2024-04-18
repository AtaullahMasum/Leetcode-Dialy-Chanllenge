
# Time Complexity is O(4*n*m)
class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        perimeter = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    perimeter += 4 # Assume the cell is surrounded by water
                    # Check adjacent cells and subtract if they are also land
                    if i > 0 and grid[i-1][j] == 1:
                        perimeter -= 1 # Top cell is land
                    if i < len(grid) - 1 and grid[i+1][j] == 1:
                        perimeter -= 1 # Bottom cell is land
                    if j > 0 and grid[i][j-1] == 1:
                        perimeter -= 1 # Left cell is land
                    if j < len(grid[0]) - 1 and grid[i][j+1] == 1:
                        perimeter -= 1 # Right cell is land
        return perimeter