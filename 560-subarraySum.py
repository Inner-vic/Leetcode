"""
    560. 和为K的子数组
    给你一个整数数组 nums 和一个整数 k ，请你统计并返回 该数组中和为 k 的子数组的个数 。
    子数组是数组中元素的连续非空序列。
"""
"""
    题目要求子数组是"连续"的，所以想到前缀和方法
    前缀和pre[i]为前i个数字的总和，pre[0]=0，pre[i] = nums[0]+nums[1]+…+nums[i-1]。
    题目要求区间和 = k，即 pre[j] - pre[i] = k => pre[i] = pre[j] - k
    第一个版本时间复杂度为O(2n)->O(n)，空间复杂度O(2n)->O(n)
    第二个版本时间复杂度为O(n)，空间复杂度O(n)
"""
from typing import List
from collections import defaultdict

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        # 前缀和数组，长度n+1
        pre_sum = [0] * (n + 1)
        for i in range(n):
            pre_sum[i+1] = pre_sum[i] + nums[i]
        # 哈希表，前缀和：前缀和出现次数
        # 注意，defaultdict(int) 键不存在时直接返回0，不会报KeyError
        cnt = defaultdict(int)
        ans = 0
        for s in pre_sum:
            # 找历史前缀和 = s - k，数量累加进答案
            ans += cnt[s - k]
            # 当前前缀和存入哈希，供后面遍历查询
            cnt[s] += 1
        return ans
    
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # 哈希表初始化：前缀和0预先出现1次，必不可少
        cnt = defaultdict(int)
        cnt[0] = 1
        cur_sum, ans = 0, 0
        for num in nums:
            # 边走边计算当前前缀和，不用额外数组
            cur_sum += num
            # 查询之前有多少前缀和等于 cur_sum - k
            ans += cnt[cur_sum - k]
            # 更新当前前缀和的出现次数
            cnt[cur_sum] += 1
        return ans