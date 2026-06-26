class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        def dfs(grid, i, j):
            if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] == '0':
                return
            grid[i][j] = '0'  # Marking it as visited

            # Explore the neighbors
            dfs(grid, i, j + 1)  # right
            dfs(grid, i, j - 1)  # left
            dfs(grid, i + 1, j)  # down
            dfs(grid, i - 1, j)  # up

        num_islands = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    num_islands += 1
                    dfs(grid, i, j)  # Marking this cell and the neighboring cells as visited ('0')

        return num_islands
