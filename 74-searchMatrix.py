"""
    74. 搜索二维矩阵
    给你一个满足下述两条属性的 m x n 整数矩阵：
     - 每行中的整数从左到右按非严格递增顺序排列。
     - 每行的第一个整数大于前一行的最后一个整数。
    给你一个整数 target ，如果 target 在矩阵中，返回 true ；否则，返回 false 。
"""
"""
    二维矩阵的二分查找，将矩阵展平成一维，大小为m*n
    a[i] = matrix[i//n][i%n]，即i整除列数，和对列数取余，注意都是列数n，没有出现行数m
    时间复杂度：O(log(mn))，空间复杂度：O(1)
"""
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        l, r = 0, m * n - 1
        while l <= r:
            mid = (l + r) // 2
            x = matrix[mid // n][mid % n]
            if x > target:
                r = mid - 1
            elif x < target:
                l = mid + 1
            else:
                return True
        return False
        