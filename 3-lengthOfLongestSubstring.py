"""
    3. 无重复字符的最长子串
    给定一个字符串 s ，请你找出其中不含有重复字符的 最长 子串 的长度。
"""
"""
    双层循环暴力求解：遍历每一个字符作为起点，找满足条件的最长的子串，维护最大值
    时间复杂度: O(n^2)，空间复杂度: O(1)
"""
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        arr = list(s)
        ans = 0
        for i in range(len(arr)):
            dic = {}
            for j in range(i, len(arr)):
                if arr[j] not in dic:
                    dic[arr[j]] = True
                else:
                    ans = max(ans, len(dic))
                    break
            ans = max(ans, len(dic))
        return ans
"""
    滑动窗口：维护窗口[left, right]内没有重复字符，右指针不断向右递增，出现重复字符时递增左指针，直到剔除重复字符，过程中更新最大窗口大小
    时间复杂度：O(2n)，每个字符会被左、右指针各访问一次；空间复杂度：O(1)
"""
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        window = set()      # set存储当前窗口所有字符，用于快速判重
        max_len = 0         # 记录无重复子串最大长度
        left, right = 0, 0
        while right < len(s):
            # 当前字符无重复，扩大右边界
            if s[right] not in window:
                window.add(s[right])        
                max_len = max(max_len, right - left + 1)
                right += 1 
            # 当前字符重复，缩小左边界，循环直到无重复字符
            else:
                window.remove(s[left])
                left += 1
        return max_len       
"""
    优化滑动窗口：字典保存字符最新下标，重复时left直接跳跃
    时间复杂度：O(n) 每个字符仅遍历一次；空间复杂度：O(1) 
"""
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_index = dict()  # key:字符 value:字符最近一次的下标
        max_len = 0
        left = 0  # 窗口左边界
        for right, ch in enumerate(s):
            # 条件1：字符出现过；条件2：字符下标>=left，代表该字符在当前窗口内
            if ch in char_index and char_index[ch] >= left:
                # 左边界直接跳到重复字符下一位，跳过所有无效区间
                left = char_index[ch] + 1
            # 更新当前字符最新下标
            char_index[ch] = right
            # 更新最大长度
            max_len = max(max_len, right - left + 1)
        return max_len