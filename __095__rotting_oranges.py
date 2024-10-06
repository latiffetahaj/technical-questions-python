'''
    994. Rotting Oranges
    You are given an m x n grid where each cell can have one of three values:
        0 representing an empty cell,
        1 representing a fresh orange, or
        2 representing a rotten orange.
        Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange becomes rotten.

    Return the minimum number of minutes that must elapse until no cell has a fresh orange. If this is impossible, return -1.

    Constraints:
        m == grid.length
        n == grid[i].length
        1 <= m, n <= 10
        grid[i][j] is 0, 1, or 2.


    #LeetCode: https://leetcode.com/problems/rotting-oranges/

    Time Complexity: O(m x n)
    Space Complexity:  O(m x n)
'''
# Use a BFS traversal algorithm simultaneously from every rotten orange
# After each level order traversal increase the minutes by 1.
# At the end if there are still fresh oranges left return -1, otherwise return minutes.

import collections
def oranges_rotting(grid):
    fresh = [0]
    q = collections.deque()

    for r in range(len(grid)):
        for c in range(len(grid[r])):
            if grid[r][c] == 2:
                q.append([r,c])

            if grid[r][c] == 1:
                fresh[0] += 1

    minutes = 0

    while q and fresh[0] > 0:
        for i in range(len(q)):
            r, c = q.popleft()

            rot_orange(r - 1, c, grid, q, fresh)
            rot_orange(r + 1, c, grid, q, fresh)
            rot_orange(r, c - 1, grid, q, fresh)
            rot_orange(r, c + 1, grid, q, fresh)

        minutes += 1

    return -1 if fresh[0] > 0 else minutes

def rot_orange(r, c, grid, q, fresh):
    if r < 0 or r >= len(grid) or c < 0 or c >= len(grid[r]) or grid[r][c] != 1:
        return

    grid[r][c] = 2
    fresh[0] -= 1
    q.append([r,c])