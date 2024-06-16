'''
    73. Set Matrix Zeroes
    Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's.
    You must do it in place.

    Constraints:
        m == matrix.length
        n == matrix[0].length
        1 <= m, n <= 200
        -2^31 <= matrix[i][j] <= 2^31 - 1

    #LeetCode: https://leetcode.com/problems/set-matrix-zeroes/

    Time Complexity: O(n x m) where n x m is the number of the elements in the matrix.

    Space Complexity: O(1)
'''
# The algorithm is to traverse the entire matrix and use the top row and first column of the matrix to store information,
# regarding which rows or which columns should we set to zero.
# The top row will hold the information of which columns should we set to zero, and this is achieved by making the first element of that column zero,
# as soon as we find a zero element.
# Similar approach is followed for rows as well.

# For testing purposes, the function returns the modified matrix.

def set_matrix_zeros(matrix):
    # This boolean is kept to hold the information for the top row.
    # Because the top row and first column intersect at [0][0], this cell is used to hold information of the 0-th column.
    # Therefore, we need an extra variable for the top_row.
    top_row = False

    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == 0:
                if i > 0:
                    # Sets the first value of that column to zero.
                    matrix[0][j] = 0

                    # Sets the first value of that row to zero.
                    matrix[i][0] = 0
                else:
                    top_row = True

    # Modify cols in range[1, end of cols index] if necessary.
    for i in range(1, len(matrix[0])):
        if matrix[0][i] == 0:
            set_column(matrix, i)

    # Modify rows in range [1, end of rows index] if necessary.
    for i in range(1, len(matrix)):
        if matrix[i][0] == 0:
            set_row(matrix, i)

    if matrix[0][0] == 0:
        set_column(matrix, 0)

    if top_row:
        set_row(matrix, 0)

    return matrix

def set_column(matrix, col_idx):

    for i in range(len(matrix)):
        matrix[i][col_idx] = 0


def set_row(matrix, row_idx):

    for i in range(len(matrix[row_idx])):
        matrix[row_idx][i] = 0

