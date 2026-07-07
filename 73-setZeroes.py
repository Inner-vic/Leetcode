"""
    73. 矩阵置零
    给定一个 m x n 的矩阵，如果一个元素为 0 ，则将其所在行和列的所有元素都设为 0 。
    请使用 原地 算法。
"""
"""
    思路：用矩阵的第一行、第一列标记需要置零的行和列，
    用两个布尔变量存首行/首列原始是否含0
    时间复杂度：O(mn)
"""
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m, n = len(matrix), len(matrix[0])
        # 标记原始第一行是否存在0
        first_row_has_zero = 0 in matrix[0]
        # 标记原始第一列是否存在0
        first_col_has_zero = False
        for item in matrix:
            if item[0] == 0:
                first_col_has_zero = True
        # 若matrix[i][j] = 0，则把所在行和所在列第一个元素置零
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == 0:
                    matrix[i][0] = matrix[0][j] = 0
        # 根据首行、首列的标记，对所在行和列元素置零
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0
        # 单独处理第一行和第一列
        if first_col_has_zero:
            for row in matrix:
                row[0] = 0
        if first_row_has_zero:
            for j in range(n):
                matrix[0][j] = 0
        