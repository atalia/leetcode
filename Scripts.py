# coding:utf-8

class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        chr_cnt = dict()
        for c in s:
            if c not in chr_cnt:
                chr_cnt[c] = 0
            chr_cnt[c] += 1
        res = []
        for c in chr_cnt.keys():
            res.append((c, chr_cnt[c]))
        res.sort(key=lambda x:x[1], reverse=True)
        result = ''
        for c,i in res:
            result += c * i
        return result


if __name__ == '__main__':
    print Solution().frequencySort('raaeaedere')
