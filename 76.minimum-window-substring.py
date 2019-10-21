#
# @lc app=leetcode id=76 lang=python
#
# [76] Minimum Window Substring
#

# @lc code=start
class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        t_d = dict()
        for c in t:
            if c not in t_d:
                t_d[c] = 0
            t_d[c] += 1
        t_size = len(t)
        cnt = 0
        left = 0
        right = 0
        s_size = len(s)
        min_cnt = s_size
        res = ""
        while right < s_size:
            while right < s_size:
                if s[right] in t_d:
                    t_d[s[right]] -= 1
                    if t_d[s[right]] >= 0:
                        cnt += 1
                        if cnt == t_size:
                            if right - left < min_cnt:
                                min_cnt = right - left
                                res = s[left:right+1]
                            right += 1
                            break
                right += 1
            while left <= right:
                if s[left] in t_d:
                    t_d[s[left]] += 1
                    if t_d[s[left]] > 0:
                        cnt -= 1
                left += 1
                if cnt == t_size:
                    if right - left - 1 < min_cnt:
                        min_cnt = right - left - 1
                        res = s[left:right]
                else:
                    break
        return res

# @lc code=end
# s = "ADOBECODEBANC"
# t = "ABC"
# print Solution().minWindow(s, t)
