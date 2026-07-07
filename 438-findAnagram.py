"""
    438. 找到字符串中所有字母异位词
    给定两个字符串 s 和 p，找到 s 中所有 p 的 异位词 的子串，返回这些子串的起始索引。不考虑答案输出的顺序。
    例:   输入: s = "cbaebabacd", p = "abc"   输出: [0,6]
"""
"""
    参考567题写法可以AC，思路相似，这里记录一种定长滑动窗口写法
"""
from collections import Counter
from typing import List

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        target = Counter(p)         #  
        window = Counter()          # 滑动窗口内字符频次
        ans = []

        for right, ch in enumerate(s):
            # 右指针指向的字符加入窗口，频次+1  
            window[ch] += 1         
            left = right - len(p) + 1       # 计算窗口左边界
            # 开始阶段，窗口长度不足，无需进行对比和移除逻辑
            if left < 0: continue
            # 当前窗口内统计频次与目标频次一致，记录起始下标
            if window == target: ans.append(left)
            # 移出窗口最左侧字符
            window[s[left]] -= 1    
            # 计数归零必须删除键，否则Counter相等判断失效
            if window[s[left]] == 0: del window[s[left]]
        
        return ans

if __name__ == "__main__":
    s = "cbaebabacd"
    p = "abc"
    solution = Solution()
    print(solution.findAnagrams(s,p))  # 输出 [0, 6]
