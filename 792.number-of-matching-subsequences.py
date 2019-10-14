#
# @lc app=leetcode id=792 lang=python
#
# [792] Number of Matching Subsequences
#
class Solution(object):
    def numMatchingSubseq(self, S, words):
        """
        :type S: str
        :type words: List[str]
        :rtype: int
        """
        w_d = dict()
        idx = 0
        for word in words:
            if word[0] not in w_d:
                w_d[word[0]] = []
            w_d[word[0]].append([idx, 1])
            idx += 1
        idx = 0
        ret = 0
        for s in S:
            if s not in w_d:
                continue
            i = 0
            tmp = w_d[s][:]
            w_d[s] = []
            while i < len(tmp):
                cur_word_index = tmp[i][0]
                next_word_pos = tmp[i][1]
                if next_word_pos >= len(words[cur_word_index]):
                    ret += 1
                    i += 1
                    continue
                c = words[cur_word_index][next_word_pos]
                if c not in w_d:
                    w_d[c] = []
                w_d[c].append([cur_word_index, next_word_pos + 1])
                i += 1
            idx += 1
        return ret


