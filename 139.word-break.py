#
# @lc app=leetcode id=139 lang=python
#
# [139] Word Break
#
class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        if s == '':
            return True
        dp = [False for _ in range(len(s)+1)]
        dp[0] = True
        record = set()
        for word in wordDict:
            record.add(word)
        for i in range(0, len(s)+1):
            for j in range(i, -1, -1):
                if dp[j]:
                    if s[j:i] in record:
                        record.add(s[:i])
                        dp[i] = True
                        break
                else:
                    continue
        return dp[-1]
