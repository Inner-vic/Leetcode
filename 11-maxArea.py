"""
    11. 盛最多水的容器
    给定一个长度为 n 的整数数组 height 。有 n 条垂线，第 i 条线的两个端点是 (i, 0) 和 (i, height[i]) 。
    找出其中的两条线，使得它们与 x 轴共同构成的容器可以容纳最多的水。
    返回容器可以储存的最大水量。
"""
"""
    题目的基本思路就是(j-i)*min(height[i],height[j])
    首先考虑的是两层循环进行遍历，用一个二维数组存每次的水量，发现不会初始化二维数组，于是只记录最大值
    (实际上确实不用定义二维数组，否则空间复杂度O(n^2))
    两层循环进行遍历的时间复杂度为O(n^2)，运行超时
    双指针法：初始化双指针，左指针->0，右指针->len(height)-1，每次移动更矮的一侧指针
    时间复杂度：O(n)
    空间复杂度：O(1)
"""
from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        ans = 0
        for i in range(len(height)):
            for j in range(i+1,len(height)):
                ans = max(ans, (j-i)*min(height[i],height[j]))
        return ans
   
class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right = 0, len(height)-1
        ans = 0
        while left < right:
            ans = max(ans, (right-left)*min(height[left],height[right]))
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1       
        return ans