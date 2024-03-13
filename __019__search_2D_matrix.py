'''
    74. Search a 2D Matrix
    You are given an m x n integer matrix matrix with the following two properties:

    Each row is sorted in non-decreasing order.
    The first integer of each row is greater than the last integer of the previous row.

    Given an integer target, return true if target is in matrix or false otherwise.

    You must write a solution in O(log(m * n)) time complexity.

    Constraints:
        m == matrix.length
        n == matrix[i].length
        1 <= m, n <= 100
        -10^4 <= matrix[i][j], target <= 10^4

    #LeetCode: https://leetcode.com/problems/search-a-2d-matrix/description/

    Time Complexity: O(log(m * n)),
                    O(log m) to search for rows + O(log n) to search in one row = O(log m) + O(log n) = O(log m * n)

    Space Complexity: O(1)
'''

def search_2D_matrix(matrix, target):
    #binary search to find on which row the target may be found => O(log m)

    top = 0
    bottom = len(matrix) - 1

    while top <= bottom:
        mid_row = top + (bottom - top) // 2

        if target < matrix[mid_row][0]:
            bottom = mid_row - 1
        elif target > matrix[mid_row][-1]:
            top = mid_row + 1
        else:
            break

    if top > bottom:
        return False

    #binary search on that row, where the target can be found => O(log n)
    row = top + (bottom - top) // 2
    low = 0
    high = len(matrix[0]) - 1

    while low <= high:
        mid = low + (high - low) // 2

        if target > matrix[row][mid]:
            low = mid + 1
        elif target < matrix[row][mid]:
            high = mid - 1
        else:
            return True

    return False