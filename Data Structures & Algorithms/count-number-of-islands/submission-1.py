class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        if grid is None:
            return counter
            
        row = len(grid) 
        col = len(grid[0])
        counter = 0

        # do dfs/bfs to mark land pieces
        def dfs(i: int, j: int):
            if i < 0 or i >= row or j < 0 or j >= col or grid[i][j] == '0':
                return
            else:
                # turn space to water
                grid[i][j] = '0'

                # check the neighbors
                dfs(i-1, j)
                dfs(i+1, j)
                dfs(i, j-1)
                dfs(i, j+1)


        # go through the grid, check if we have a '1' or '0'.

        for i in range(row):
            for j in range(col):
                # if 1, increment counter and exhaust the neighbouring land pieces
                if grid[i][j] == '1':
                    counter += 1
                    # do dfs
                    dfs(i ,j)
                # if 0, skip it
                else:
                    continue
        
        return counter