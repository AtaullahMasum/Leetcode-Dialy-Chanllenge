class Solution:
    def dfs (self, row, col, visited, dir, grid, rows, cols):
        visited.add((row, col))
        for dr, dc in dir:
            new_row = row + dr
            new_col = col + dc
            if 0 <= new_row < rows and 0 <= new_col < cols and (new_row, new_col) not in visited and grid[new_row][new_col] == "1":
                self.dfs(new_row, new_col, visited, dir, grid, rows, cols)
    
    def numIslands(self, grid: List[List[str]]) -> int:
        dir = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        rows = len(grid)
        cols = len(grid[0])
        cnt = 0
        visited = set()
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == "1" and (row, col) not in visited:
                    cnt += 1
                    self.dfs(row, col, visited, dir, grid, rows, cols)
        return cnt
        