#
# @lc app=leetcode id=14 lang=python
#
# [14] Longest Common Prefix
#

# @lc code=start
class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) < 1:
            return ""
        prefix = strs[0]
        for substr in strs:
            idx = 0
            idx_max = min(len(prefix), len(substr))
            while idx < idx_max and prefix[idx] == substr[idx]:
                idx += 1
            if idx == 0:
                return ""
            else:
                prefix = prefix[0:idx]
        return prefix

#print Solution().longestCommonPrefix(["dog","racecar","car"])
# @lc code=end

