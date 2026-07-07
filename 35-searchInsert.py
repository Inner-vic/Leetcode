"""
    35. 搜索插入位置
    给定一个排序数组和一个目标值，在数组中找到目标值，并返回其索引。如果目标值不存在于数组中，返回它将会被按顺序插入的位置。
    请必须使用时间复杂度为 O(log n) 的算法。
"""
"""
    二分查找，习惯用闭区间[left, right]表示
    初始化为left->0，right->len-1
    更新过程中，由于采用闭区间，所以不匹配的时候，mid一定不是最终结果，left->mid+1，right->mid-1
    时间复杂度：O(logn)，空间复杂度：O(1)
"""
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)-1
        while l <= r :
            mid = (l + r) // 2
            if nums[mid] < target:
                l = mid + 1
            elif nums[mid] > target:
                r = mid - 1
            else:
                return mid
        return l