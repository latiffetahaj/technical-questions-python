'''
    36. Valid Sudoku

    Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

    Rules:
    Each row must contain the digits 1-9 without repetition.
    Each column must contain the digits 1-9 without repetition.
    Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
    Note:

    A Sudoku board (partially filled) could be valid but is not necessarily solvable.
    Only the filled cells need to be validated according to the mentioned rules.

    Time Complexity: O(n^2)

    Space Complexity: O(n^2)

'''
from collections import defaultdict

def isValidSudoku(board):

    hash_box = defaultdict(list)

    for i in range(9):
        hash_row = set()
        hash_column = set()
        for j in range(9):
            if board[i][j].isdigit():

                #row check
                if board[i][j] not in hash_row:
                    hash_row.add(board[i][j])
                else:
                    return False

                # 3x3 boxes check
                if board[i][j] not in hash_box[i//3,j//3]:
                    hash_box[i//3,j//3].append(board[i][j])
                else:
                    return False


            if board[j][i].isdigit():

                #column check
                if board[j][i] not in hash_column:
                    hash_column.add(board[j][i])
                else:
                    return False

    return True
