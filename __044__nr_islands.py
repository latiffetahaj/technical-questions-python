'''
    200. Number of Islands
    Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.
    An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically.
    You may assume all four edges of the grid are all surrounded by water.

    Constraints:
        m == grid.length
        n == grid[i].length
        1 <= m, n <= 300
        grid[i][j] is '0' or '1'.


    #LeetCode: https://leetcode.com/problems/number-of-islands/description/

    Time Complexity: O(m x n) each cell will be visited at most twice, m x n is the size of the 2D grid
    Space Complexity: O(m x n)
'''
#algorithm is to traverse the entire grid and when a land is encountered to
#perform a depth-first search to find its land neighbors and mark them as visited
def nr_islands(grid):
    if not grid or len(grid) == 0:
        return 0

    ROWS = len(grid)
    COLS = len(grid[0])
    nr_islands = 0
    visited = set()

    def dfs(r,c,grid):
        if (not (r >=0 and r < ROWS) #out of bounds for rows
            or not (c >=0 and c < COLS) #out of bounds for columns
            or (r,c) in visited #check if already visited
            or grid[r][c] == '0'):#or if it is water
            return

        #mark the current location as visited
        visited.add((r,c))

        #generate neighbors, up, down, left, right
        neighbors = [[r + 1,c], [r - 1, c], [r, c - 1], [r, c + 1]]

        for new_r, new_c in neighbors:
            #perform dfs on the neighbors of the current location
            dfs(new_r,new_c,grid)

        return

    #traverse the entire grid
    for r in range(ROWS):
        for c in range(COLS):
            if grid[r][c] == '1' and (r,c) not in visited:
                nr_islands += 1
                dfs(r,c,grid)


    return nr_islands