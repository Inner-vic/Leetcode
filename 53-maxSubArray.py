"""
    53. 最大子数组和
    给你一个整数数组 nums ，请你找出一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。
    子数组是数组中的一个连续部分。
"""
"""
    返回‘连续’子数组和的最大值，首先想到前缀和，最大子数组和 =（当前前缀和-前序最小前缀和）中的最大值
    在计算前缀和的过程中需要维护最小前缀和
    时间复杂度：O(n)，空间复杂度：O(1)
"""
from cmath import inf
from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:  
        pre_sum = min_pre = 0
        ans = -inf
        for n in nums:
            pre_sum += n                        # 计算前缀和
            ans = max(ans, pre_sum - min_pre)   # 当前前缀和 - 前序最小前缀和，记录最大值
            min_pre = min(min_pre, pre_sum)     # 维护最小前缀和
        return ans
    