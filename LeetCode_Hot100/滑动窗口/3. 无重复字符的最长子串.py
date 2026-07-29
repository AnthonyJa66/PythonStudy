# 3. 无重复字符的最长子串
#
# 提示
# 给定一个字符串 s ，请你找出其中不含有重复字符的最长子串 的长度。
#
# 示例 1:
#
# 输入: s = "abcabcbb"
# 输出: 3
# 解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。注意 "bca" 和 "cab" 也是正确答案。
# 示例 2:
#
# 输入: s = "bbbbb"
# 输出: 1
# 解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。
# 示例 3:
#
# 输入: s = "pwwkew"
# 输出: 3
# 解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。
# 请注意，你的答案必须是 子串 的长度，"pwke" 是一个子序列，不是子串。
#
#
# 提示：
#
# 0 <= s.length <= 5 * 104
# s 由英文字母、数字、符号和空格组成

from collections import defaultdict


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        # list1=list(s)
        # n = len(list1)
        dict= {}
        left=0
        max_len=0
        for right in range(len(s)):

            temp=s[right]#将当前字符赋值给temp

            if temp in dict and dict[temp]>= left:#如果当前字符在字典中，并且它的索引大于等于left，说明当前字符在当前子串中出现过
                left=dict[temp]+1    #将left更新为当前字符的索引加1，将当前字符从当前子串中移除

            dict[temp]=right#将当前字符的索引赋值给字典中的temp键，如{"a":0,"b":1,"c":2,"b":3,"c":4}，说明当前子串为"abc"，长度为3
            # print(dict)
            max_len=max(max_len,right-left+1)#将当前子串的长度与max_len进行比较，取较大值

        return max_len









s1="shjkfbjsb"
# lc={}
# lc["r"]=5
# print(lc)
# list2=list(s1)
# dict1=defaultdict(int)
# print(dict1)

ss=Solution()
print(ss.lengthOfLongestSubstring(s1))



