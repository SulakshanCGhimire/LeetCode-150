"""
Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's.

You must do it in place.
 

Example 1:

    Input: matrix = [[1,1,1],[1,0,1],[1,1,1]]
    Output: [[1,0,1],[0,0,0],[1,0,1]]
    
Example 2:

    Input: matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
    Output: [[0,0,0,0],[0,4,5,0],[0,3,1,0]]
 

Constraints:

    m == matrix.length
    n == matrix[0].length
    1 <= m, n <= 200
    -231 <= matrix[i][j] <= 231 - 1
"""

from typing import List


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        rows, cols = len(matrix), len(matrix[0])

        first_row_zero = False
        first_col_zero = False

        # Check if first row contains zero
        for c in range(cols):
            if matrix[0][c] == 0:
                first_row_zero = True
                break

        # Check if first column contains zero
        for r in range(rows):
            if matrix[r][0] == 0:
                first_col_zero = True
                break

        # Use first row and column as markers
        for r in range(1, rows):
            for c in range(1, cols):
                if matrix[r][c] == 0:
                    matrix[r][0] = 0
                    matrix[0][c] = 0

        # Zero marked rows
        for r in range(1, rows):
            if matrix[r][0] == 0:
                for c in range(1, cols):
                    matrix[r][c] = 0

        # Zero marked columns
        for c in range(1, cols):
            if matrix[0][c] == 0:
                for r in range(1, rows):
                    matrix[r][c] = 0

        # Zero first row if needed
        if first_row_zero:
            for c in range(cols):
                matrix[0][c] = 0

        # Zero first column if needed
        if first_col_zero:
            for r in range(rows):
                matrix[r][0] = 0