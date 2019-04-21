# coding:utf-8


class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        length = len(s) + 1
        dp = [0 for i in range(length)]
        dp[0] = 1
        dp[1] = 1 if s[0] != '0' else 0
        for i in xrange(2, length):
            if 10 <= int(s[i-2:i]) <= 26:
                dp[i] = dp[i-2]
            if s[i-1] != '0':
                dp[i] += dp[i-1]
        return dp[length-1]

if __name__ == '__main__':
    #print Solution().numDecodings('12')
    #print Solution().numDecodings('226')
    #print Solution().numDecodings('10')
    #print Solution().numDecodings('0')
    #print Solution().numDecodings('100')
    #print Solution().numDecodings('110')
    #print Solution().numDecodings('4085393587263438197362839792651187379538211951318577884164713291143976212416731331985661435443671959')
