#
# @lc app=leetcode id=338 lang=python
#
# [338] Counting Bits
#
class Solution(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        self.result = [0 for i in range(num + 1)]
        self.cn = [0 for i in range(num + 1)]
        sn = 0
        for i in range(1, num + 1):
            if i & (i - 1) == 0:
                sn = i
                self.cn[i] = sn
                self.result[i] = 1
            else:
                self.cn[i] = sn
                self.result[i] = self.find_cn(i)
        return self.result

    def find_cn(self, num):
        if num == 0 or self.result[num] != 0:
            return self.result[num]
        self.result[num] = 1 + self.find_cn(num - self.cn[num])
        return self.result[num]
