#
# @lc app=leetcode id=524 lang=python
#
# [524] Longest Word in Dictionary through Deleting
#
class Solution(object):
    def findLongestWord(self, s, d):
        """
        :type s: str
        :type d: List[str]
        :rtype: str
        """
        max_cnt = 0
        res = ''
        for x in d:
            _cnt = self._is_in(s, x)
            if _cnt > max_cnt:
                res = x
                max_cnt = _cnt
            elif _cnt == max_cnt and _cnt != 0:
                if len(x) > len(res):
                    res = x
                elif len(x) == len(res):
                    res = min(res, x)
        return res
    
    def _is_in(self, s, d):
        cnt = 0
        size_s = len(s)
        size_d = len(d)
        s_idx = 0
        d_idx = 0
        while s_idx < size_s and d_idx < size_d:
            if s[s_idx] == d[d_idx]:
                d_idx += 1
                cnt += 1
            s_idx += 1
        if d_idx != size_d:
            return -1
        return cnt

