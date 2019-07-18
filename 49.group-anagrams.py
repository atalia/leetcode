#
# @lc app=leetcode id=49 lang=python
#
# [49] Group Anagrams
#
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        _str_map = dict()
        for s in strs:
            k = ''.join((lambda x: (x.sort(),x)[1])(list(s)))
            if not _str_map.has_key(k):
                _str_map[k] = []
            _str_map[k].append(s)
        result = []
        for s in _str_map.itervalues():
            result.append(s)
        return result
        

