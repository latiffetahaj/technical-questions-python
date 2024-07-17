'''
    62. Unique Paths
    There is a robot on an m x n grid.
    The robot is initially located at the top-left corner (i.e., grid[0][0]).
    The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]).
    The robot can only move either down or right at any point in time.

    Given the two integers m and n, return the number of possible unique paths that the robot can take to reach the bottom-right corner.
    The test cases are generated so that the answer will be less than or equal to 2 * 109.

    Constraints:
        1 <= m, n <= 100


    #LeetCode: https://leetcode.com/problems/unique-paths/

    Time Complexity: O(n x m)

    Space Complexity: O(n x m)
'''
# The algorithm is a bottom up dynamic programming.
def unique_paths(m ,n):
    # Initialize a grid of m x n.
    grid = [[0] * m for i in range(n)]

    # Initialize the last cell to 1 because whenever we visit that cell, it means that we found 1 unique path.
    grid[n - 1][m - 1] = 1

    for i in range(n - 1, -1, -1):

        for j in range(m - 1, -1, -1):
            # In each cell the number of unique paths is the sum of unique paths from right and unique paths from down.
            # Look to the right.
            if j + 1 < m:
                grid[i][j] += grid[i][j + 1]

            # Look down.
            if i + 1 < n:
                grid[i][j] += grid[i + 1][j]


    return grid[0][0]
