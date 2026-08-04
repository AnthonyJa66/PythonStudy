#给定两个字符串 s 和 p，找到 s 中所有 p 的 异位词 的子串，返回这些子串的起始索引。不考虑答案输出的顺序。

# 示例 1:
#
# 输入: s = "cbaebabacd", p = "abc"
# 输出: [0,6]
# 解释:
# 起始索引等于 0 的子串是 "cba", 它是 "abc" 的异位词。
# 起始索引等于 6 的子串是 "bac", 它是 "abc" 的异位词。
#  示例 2:
#
# 输入: s = "abab", p = "ab"
# 输出: [0,1,2]
# 解释:
# 起始索引等于 0 的子串是 "ab", 它是 "ab" 的异位词。
# 起始索引等于 1 的子串是 "ba", 它是 "ab" 的异位词。
# 起始索引等于 2 的子串是 "ab", 它是 "ab" 的异位词。
#
#
# 提示:
#
# 1 <= s.length, p.length <= 3 * 104
# s 和 p 仅包含小写字母

from typing import List

from sqlalchemy.util import counter


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:

        #超时了
        # n, m = len(s), len(p)
        # if  n < m:return []
        # result = []
        # p1=sorted(p)
        #
        # for i in range(n - m + 1):
        #     if sorted(s[i:i + m]) == p1:
        #         result.append(i)

        #滑动窗口
        n, m = len(s), len(p)

        if n < m:
            return []

        ans = []
        s_count = [0] * 26
        p_count = [0] * 26
        for item in p:
            p_count[ord(item)-97]+=1
        for i in range(m-1):
            s_count[ord(s[i])-97]+=1

        for i in range(m-1,n):
            s_count[ord(s[i])-97]+=1
            if s_count==p_count:
                ans.append(i-m+1)

            s_count[ord(s[i-m+1])-97]-=1

        return ans




a="kjhj"
print(ord(a[2]),ord('a'))
print(ord('a'))
p=[0]*26
p[ord(a[2])-97]+=1
print(p)
# print(Solution().findAnagrams(a,p))

