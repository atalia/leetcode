#
# @lc app=leetcode id=1071 lang=python
#
# [1071] Greatest Common Divisor of Strings
#

# @lc code=start
class Solution(object):
    def gcdOfStrings(self, str1, str2):
        """
        :type str1: str
        :type str2: str
        :rtype: str
        """
        str1_len = len(str1)
        str2_len = len(str2)
        if str1_len < str2_len:
            str1 , str2 = str2 , str1
            str1_len, str2_len = str2_len, str1_len
        if str1[0:str2_len] != str2:
            return ""
        if not str1[str2_len:]:
            return str1
        return self.gcdOfStrings(str2, str1[str2_len:])

#print Solution().gcdOfStrings("TAUXXTAUXXTAUXXTAUXXTAUXX", "TAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXX")
# @lc code=end

