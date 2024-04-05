'''
Count islands.
Given a map as a 2d array. An island is a group of 1s that are all connected left/right/up/down.
Count and return the number of islands in the map.

Time Complexity: O(n * m) where n*m is the size of the matrix
Space Complexity: O(n * m) for recursive calls + O(n * m) for the set, ==> O(n * m)
'''


#algorithm is to traverse the entire grid and when a land is encountered to
#perform a depth-first search to find its land neighbors and mark them as visited
def num_islands(grid):
    if not grid:
        return 0

    #get the size of the grid
    ROWS = len(grid)
    COLS = len(grid[0])
    visited = set()
    nr_islands = 0

    #iterate over all elements of the grid
    for r in range(ROWS):
        for c in range(COLS):
            #when 1 is encountered and not visited, call dfs to find if it has any neighbors that need to be marked visited
            if grid[r][c] == "1" and (r,c) not in visited:
                nr_islands += 1
                dfs(grid, r, c, visited, ROWS, COLS)

    return nr_islands


def dfs(grid, r, c, visited, ROWS, COLS):

    if (not (r >=0 and r < ROWS) #out of bounds for rows
    or not (c >= 0 and c < COLS) #out of bounds for coloumns
    or grid[r][c] == "0" #if it is a zero, means water
    or (r, c) in visited): # already visited
        return

    #add to visited set
    visited.add((r, c))

    #get the 4 neighbors, up, down, right, left
    neighbors = [[r - 1, c], [r + 1, c], [r, c + 1], [r, c - 1]]

    #do a depth-first search in the neighbors
    for new_r, new_c in neighbors:
        dfs(grid, new_r, new_c, visited, ROWS, COLS)

    return


def main():
    grid = [["1","1","1","1","0"],
            ["1","1","0","1","0"],
            ["1","1","0","0","0"],
            ["0","0","0","0","1"]]

    print(num_islands(grid))

if __name__ == '__main__':
    main()