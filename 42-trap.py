"""
    42. 接雨水
    给定 n 个非负整数表示每个宽度为 1 的柱子的高度图，计算按此排列的柱子，下雨之后能接多少雨水。
"""
"""
    思路：每一根柱子能存的水量 = min(柱左侧最大高度,柱右侧最大高度) - 当前柱子高度
    左边最高：pre_max[i]，从左往右遍历记录到 i 为止的最大高度
    右边最高：suf_max[i]，从右往左遍历记录到 i 为止的最大高度
    若 min(左最大, 右最大) > 当前高度，差值就是该位置储水量；否则存不了水
    时间复杂度：O(3n)->O(n)；   空间复杂度：O(2n)->O(n)
"""
class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)

        pre_max = [0] * n
        pre_max[0] = height[0]
        for i in range(1, n):
            pre_max[i] = max(pre_max[i-1], height[i])
        
        suf_max = [0] * n
        suf_max[-1] = height[-1]
        for i in range(n-2, -1, -1):
            suf_max[i] = max(suf_max[i+1], height[i])

        ans = 0
        for h, pre, suf in zip(height, pre_max, suf_max):
            ans += min(pre, suf) - h
        return ans
        