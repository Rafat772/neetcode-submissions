class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        rows = len(grid)
        cols = len(grid[0])

        count = 0

        def dfs(r, c):

            # Boundary check
            if r < 0 or r >= rows or c < 0 or c >= cols:
                return

            # If water, stop
            if grid[r][c] == '0':
                return

            # Mark land as visited
            grid[r][c] = '0'

            # Visit up
            dfs(r - 1, c)

            # Visit down
            dfs(r + 1, c)

            # Visit left
            dfs(r, c - 1)

            # Visit right
            dfs(r, c + 1)

        for r in range(rows):
            for c in range(cols):

                if grid[r][c] == '1':

                    # Found a new island
                    count += 1

                    # Visit entire island
                    dfs(r, c)

        return count