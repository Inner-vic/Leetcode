"""
    283. 移动零
    给定一个数组 nums，编写一个函数将所有 0 移动到数组的末尾，同时保持非零元素的相对顺序。
    请注意 ，必须在不复制数组的情况下原地对数组进行操作。
"""
"""
    方法一：双指针
    已经提示是双指针题目，所以自然而言的使用双指针，快指针查找非0元素，慢指针记录非0元素
    快指针遍历完数组后，nums[0,slow-1]是慢指针记录的所有非零元素，nums[slow:]的值没变，需要补零
    时间复杂度：O(n)
    空间复杂度：O(1)
"""
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        fast, slow = 0, 0
        while fast < len(nums):
            if nums[fast] != 0:
                nums[slow] = nums[fast]
                slow += 1
            fast += 1
        for i in range(slow, len(nums)):
            nums[i] = 0
"""
    ※方法二：双指针+交换元素（参考题解）
    优点只需要一轮循环，不需要再循环一次补零
    时间复杂度：O(n)
    空间复杂度：O(1)
"""
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        fast, slow = 0, 0
        while fast < len(nums):
            if nums[fast] != 0:
                nums[fast], nums[slow] = nums[slow], nums[fast]
                slow += 1
            fast += 1

