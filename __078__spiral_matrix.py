'''
    54. Spiral Matrix
    Given an m x n matrix, return all elements of the matrix in spiral order.

    Constraints:
        m == matrix.length
        n == matrix[i].length
        1 <= m, n <= 10
        -100 <= matrix[i][j] <= 100

    #LeetCode: https://leetcode.com/problems/spiral-matrix/

    Time Complexity: O(n x m) where n x m is the number of the elements in the matrix.

    Space Complexity: O(n x m) to hold the result.
'''

def spiral_matrix(matrix):
    result = []
    # Column pointers.
    left, right = 0, len(matrix[0]) - 1

    # Row pointers.
    top, bottom = 0, len(matrix) - 1

    while left <= right and top <= bottom:

        for i in range(right - left + 1):
            result.append(matrix[top][left + i])

        top += 1

        for i in range(bottom - top + 1):
            result.append(matrix[top + i][right])

        right -= 1

        if not (left <= right and top <= bottom):
            break

        for i in range(right - left + 1):
            result.append(matrix[bottom][right - i])

        bottom -= 1

        for i in range(bottom - top + 1):
            result.append(matrix[bottom - i][left])

        left += 1

    return result
