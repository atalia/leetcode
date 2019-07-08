#
# @lc app=leetcode id=392 lang=python
#
# [392] Is Subsequence
#
class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        size_s = len(s)
        size_t = len(t)
        si = 0
        ti = 0
        match = 0
        while si < size_s:
            while ti < size_t and s[si] != t[ti]:
                ti += 1
            if ti < size_t and s[si] == t[ti]:
                si += 1
                ti += 1
                match += 1
            if ti == size_t:
                break
        if match != size_s :
            return False
        return True

            
