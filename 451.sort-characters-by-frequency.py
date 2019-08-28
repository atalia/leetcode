#
# @lc app=leetcode id=451 lang=python
#
# [451] Sort Characters By Frequency
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
        heap = []
        for c in chr_cnt.keys():
            heap.append(c)
            size = len(heap) - 1
            while size > 0 and chr_cnt[heap[size/2]] < chr_cnt[c]:
                heap[size] = heap[size/2]
                size /= 2
            heap[size] = c
        result = ''
        while heap:
            c = heap[0]
            result += c * chr_cnt[c]
            x = heap[-1]
            heap.pop()
            i = 0
            while(2 * i + 1 < len(heap)):
                child = 2 * i + 1
                if(child + 1 < len(heap) and chr_cnt[heap[child]] < chr_cnt[heap[child + 1]]):
                    child += 1
                if(chr_cnt[heap[child]] > chr_cnt[x]):
                    heap[i], heap[child] = heap[child], heap[i]
                else:
                    break
                i = child
            if heap:
                heap[i] = x
        return result





