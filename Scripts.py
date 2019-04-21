# coding:utf-8

class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        a = a if len(a) > len(b) else '0' * (len(b)-len(a)) + a
        b = b if len(b) > len(a) else '0' * (len(a)-len(b)) + b
        result = ['0' for i in xrange(len(a) + 1)]
        bit = 0
        for i in xrange(len(a)-1, -1, -1):
            ai = 1 if a[i] == '1' else 0
            bi = 1 if b[i] == '1' else 0
            ai = ai + bi + bit
            if ai >= 2:
                result[i] = '0' if ai == 2 else '1'
                bit = 1
            else:
                result[i] = '1' if ai == 1 else '0'
                bit = 1
        result[0] = '1' if bit == 1 else '0'
        return ''.join(result)

if __name__ == '__main__':
    print Solution().addBinary('1010','1011')
