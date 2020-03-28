#
# @lc app=leetcode id=820 lang=python
#
# [820] Short Encoding of Words
#

# @lc code=start
class Solution(object):
    def minimumLengthEncoding(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        words.sort(key=lambda x: x[::-1], reverse=True)
        base = ""
        ret = 0
        for word in words:
            if word not in base:
                base = word
                ret += len(base) + 1
        return ret

#words = ["time", "me", "bell"]
#print Solution().minimumLengthEncoding(words)
# @lc code=end

