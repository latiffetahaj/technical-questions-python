'''
    Islands and Treasure
    You are given a m x n 2D grid initialized with these three possible values:
        1. -1 - A water cell that can not be traversed.
        2. 0 - A treasure chest.
        3. INF - A land cell that can be traversed.

    We use the integer 2^31 - 1 = 2147483647 to represent INF.

    Fill each land cell with the distance to its nearest treasure chest.
    If a land cell cannot reach a treasure chest than the value should remain INF.

    Assume the grid can only be traversed up, down, left, or right.

    Constraints:
        m == grid.length
        n == grid[i].length
        1 <= m, n <= 100
        grid[i][j] is one of {-1, 0, 2147483647}.


    #LeetCode: https://leetcode.com/problems/walls-and-gates/

    Time Complexity: O(m x n) for visiting each cell at most twice.
    Space Complexity: O(m x n) for the queue.
'''
import collections

# Reverse thinking for this problem.
# Start at the treasure and do a BFS, a level order traversal of the grid.
# The BFS is done simultaneously from all the treasure cells.
# First level we explore locations that are 1 distance away from treasure, then 2 distance away and so on.
def walls_and_gates(grid):
    visited = set()
    q = collections.deque()

    for r in range(len(grid)):
        for c in range(len(grid[r])):
            if grid[r][c] == 0:
                q.append([r,c])
                visited.add((r,c))

    distance = 0

    while q:
        for i in range(len(q)):
            r, c = q.popleft()

            grid[r][c] = distance

            explore(r - 1, c, grid, visited, q)
            explore(r + 1, c, grid, visited, q)
            explore(r, c - 1, grid, visited, q)
            explore(r, c + 1, grid, visited, q)

        distance += 1



def explore(r, c, grid, visited, q):
    if (r < 0 or r >= len(grid)
        or c < 0 or c >= len(grid[r])
        or (r, c) in visited
        or grid[r][c] == -1):
        return

    q.append([r,c])
    visited.add((r, c))