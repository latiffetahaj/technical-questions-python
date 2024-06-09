'''
    417. Pacific Atlantic Water Flow
    There is an m x n rectangular island that borders both the Pacific Ocean and Atlantic Ocean.
    The Pacific Ocean touches the island's left and top edges, and the Atlantic Ocean touches the island's right and bottom edges.
    The island is partitioned into a grid of square cells.
    You are given an m x n integer matrix heights where heights[r][c] represents the height above sea level of the cell at coordinate (r, c).
    The island receives a lot of rain, and the rain water can flow to neighboring cells directly north, south, east, and west if the neighboring cell's height is less than or equal to the current cell's height.
    Water can flow from any cell adjacent to an ocean into the ocean.
    Return a 2D list of grid coordinates result where result[i] = [ri, ci] denotes that rain water can flow from cell (ri, ci) to both the Pacific and Atlantic oceans.

    Constraints:
        m == heights.length
        n == heights[r].length
        1 <= m, n <= 200
        0 <= heights[r][c] <= 105


    #LeetCode: https://leetcode.com/problems/pacific-atlantic-water-flow/

    Time Complexity: O(m x n)
    Space Complexity: O(m x n)
'''
# We do a DFS from the edge of the 2D array going towards inside.
# We build two sets, one with all the cells that can reach the Atlantic Ocean, the other with Pacific ocean.
# Then then intersection between two sets is the result.
def pacific_atlantic(heights):
    result = []
    pac, atl = set(), set()
    ROWS, COLS = len(heights), len(heights[0])

    for c in range(COLS):
        dfs(0,c, pac, heights, heights[0][c])
        dfs(ROWS - 1,c, atl, heights, heights[ROWS - 1][c])

    for r in range(ROWS):
        dfs(r, 0, pac, heights, heights[r][0])
        dfs(r, COLS - 1, atl, heights, heights[r][COLS - 1])

    for i in range(ROWS):
        for j in range(COLS):
            if (i,j) in pac and (i,j) in atl:
                result.append([i,j])


    return result


def dfs(r, c, visited, heights, prev_height):
    if (r < 0 or c < 0
        or r >= len(heights) or c >= len(heights[r])
        or (r,c) in visited
        or prev_height > heights[r][c]): # If prev_height is larger than current_height, that means the water can't flow from current_height to prev_height.
        return

    visited.add((r,c))
    neighbors = [[r - 1, c], [r + 1, c], [r, c - 1], [r, c + 1]]

    for new_r, new_c in neighbors:
        dfs(new_r, new_c, visited, heights, heights[r][c])

    return