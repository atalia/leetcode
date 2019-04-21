# coding:utf-8


class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        nums = s.split('0')
        result = 1
        for num in nums:
            result *= self.deocding(num)
        return result

    def deocding(self, s):
        if s == '':
            return 1
        if len(s) == 1:
            return 1
        if 1 <= int(s[0]) <=2 and 1 <= int(s[1]) <= 6:
            return self.deocding(s[2:]) * 2
        else:
            return self.deocding(s[2:]) * 1

if __name__ == '__main__':
    S = Solution()
    print S.numDecodings('226')