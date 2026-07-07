"""
    567. 字符串的排列
    给你两个字符串 s1 和 s2 ，写一个函数来判断 s2 是否包含 s1 的 排列。如果是，返回 true ；否则，返回 false 。
    换句话说，s1 的排列之一是 s2 的 子串 。
"""
"""
    438题解不出来，先来做567题，采用滑动窗口，思路很简单，但问题有：
    1. 不知道Counter()函数，当然也可以用for循环遍历：
        for item in s: 
            dic[item] = dic.get(item, 0) + 1
    2. 不知道del操作
"""
from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n1, n2 = len(s1), len(s2)
        
        count1 = Counter(s1)        # dict类型，统计s1字符出现的频次
        count2 = Counter(s2[:n1])   # 初始化，并统计s2第一个滑动窗口（长度n1）

        # 判断第一个窗口是否满足
        if count1 == count2:
            return True
        # i代表当前窗口新进入的右侧字符下标，从n1开始遍历到末尾
        for i in range(n1, n2):
            count2[s2[i]] += 1      # 加入滑动窗口的新字符计数+1
            count2[s2[i-n1]] -= 1   # 移出滑动窗口的旧字符计数-1
            # 注意：若计数为0，需要删除该键，否则相等判断会失效
            if count2[s2[i-n1]] == 0:
                del count2[s2[i-n1]]
            if count1 == count2:
                return True
        return False
