'''
    48. Rotate Image
    You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).
    You have to rotate the image in-place, which means you have to modify the input 2D matrix directly.
    DO NOT allocate another 2D matrix and do the rotation.

    Constraints:
        n == matrix.length == matrix[i].length
        1 <= n <= 20
        -1000 <= matrix[i][j] <= 1000

    #LeetCode: https://leetcode.com/problems/rotate-image/

    Time Complexity: O(n^2) where n is the size of the matrix.

    Space Complexity: O(1)
'''
# For testing purposes, the function returns the modified matrix.

def rotate_image_90(matrix):
    # These are pointers to move along columns.
    left, right = 0, len(matrix[0]) - 1

    while left < right:
        for i in range(right - left):
            # These are pointers to move along rows.
            top = left
            bottom = right

            top_left = matrix[top][left + i]

            matrix[top][left + i] = matrix[bottom - i][left]

            matrix[bottom - i][left] = matrix[bottom][right - i]

            matrix[bottom][right - i] = matrix[top + i][right]

            matrix[top + i][right] = top_left

        left += 1
        right -= 1


    return matrix