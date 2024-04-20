class Solution:
    def dfs(self, land, row, col, visited, dir,bottom_right):
        for dr, dc in dir:
            nr, nc = row + dr , col + dc
            if 0 <= nr < len(land) and 0 <= nc < len(land[0]) and land[nr][nc] == 1 and (nr, nc) not in visited:
                visited.add((nr, nc))
                bottom_right[0] = max(bottom_right[0], nr)
                bottom_right[1] = max(bottom_right[1], nc)
                self.dfs(land, nr, nc, visited, dir,bottom_right)


    def findFarmland(self, land: List[List[int]]) -> List[List[int]]:
        ans = []
        visited = set()
        dir = [(1, 0), (0, 1)]
        for row in range(len(land)):
            for col in range(len(land[0])):
                if land[row][col] == 1 and (row, col) not in visited:
                    visited.add((row, col)) 
                    top_left = [row, col]
                    bottom_right = [row, col] 
                    self.dfs(land, row, col, visited, dir,bottom_right)
                    ans1  = top_left + bottom_right
                    ans.append(ans1)
        return ans
