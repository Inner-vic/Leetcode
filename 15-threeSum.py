"""
    15. 三数之和
    给你一个整数数组 nums ，判断是否存在三元组 [nums[i], nums[j], nums[k]] 满足 i != j、i != k 且 j != k ，
    同时还满足 nums[i] + nums[j] + nums[k] == 0 。请你返回所有和为 0 且不重复的三元组。
    注意：答案中不可以包含重复的三元组。
"""
"""
    最先想到的是两层循环，利用等式nums[i] + nums[j] = -nums[k]，没有AC，遇到的问题：
    1. 列表list不能存入哈希表 -> 可以转元组tuple
    2. 哈希表存的不能是下标，因为nums中可能存在重复数字
    例如[-1,0,1,-1]，其中(0,1,2)->[-1,0,1]; (1,2,3)->[0,1,-1]，下标不同但结果是同一三元组
    两层循环时间复杂度为O(n^2)，没有写出来，下面的三层循环暴力求解，时间复杂度O(n^3)
"""
class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        hashtable = {}
        ans = []
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                for k in range(j+1, len(nums)):
                    if nums[i] + nums[j] + nums[k] == 0:
                        trp = tuple(sorted([nums[i], nums[j], nums[k]]))
                        if trp not in hashtable:
                            hashtable[trp] = True
                            ans.append(list(trp))
        return ans
"""
    最优解法（排序+双指针）提示：排序、双指针
    重点和难点在于去重：外层去重，然后双指针部分需要去重
    时间复杂度：O(n*logn) + O(n*n) = O(n^2)
"""
class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()                     # 排序，时间复杂度O(n*logn)
        ans = []
        for i in range(len(nums)):      # 外层for循环时间复杂度O(n)
            # 外层去重，避免产生重复的三元组
            if i > 0 and nums[i] == nums[i-1]:
                continue

            left, right = i+1, len(nums)-1
            while left < right:         # 内层双指针遍历时间复杂度O(n)
                total = nums[i] + nums[left] + nums[right]
                if total == 0:
                    # 三数之和为0，符合要求，加入ans
                    ans.append([nums[i], nums[left], nums[right]])
                    # 左指针去重，跳过与nums[left]重复的值
                    while left < right and nums[left] == nums[left+1]:
                        left += 1
                    # 右指针去重，跳过与nums[right]重复的值
                    while left < right and nums[right] == nums[right-1]:
                        right -= 1
                    left += 1
                    right -= 1
                elif total > 0:
                    # 如果三数之和大于0，需要加一个更小的数，右指针左移
                    right -= 1
                elif total < 0:
                    # 如果三数之和小于0，需要加一个更大的数，左指针右移
                    left += 1
        return ans

        
        