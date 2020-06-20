# coding:utf-8
# @lc app=leetcode id=438 lang=python
#
# [438] Find All Anagrams in a String
#

# @lc code=start
class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        start = 0
        end = 0
        match = 0
        counter = self.counter(p)
        idx = 0
        ret = []
        while start <= len(s) - len(p):
            while end < len(s) and s[end] in counter:
                if counter[s[end]] > 0:
                    counter[s[end]] -= 1
                    match += 1 
                    if match == len(p):
                        ret.append(start)
                        match -= 1
                        counter[s[start]] += 1
                        start += 1
                    end += 1
                elif s[start] == s[end]:
                    start += 1
                    end += 1
                else:
                    while start < end:
                        counter[s[start]] += 1
                        match -= 1
                        if s[start] == s[end]:
                            start += 1
                            break
                        start += 1
            end += 1    
            start = end
            counter = self.counter(p)
            match = 0
        return ret
    
    def counter(self, p):
        d = dict()
        for p_e in p:
            if p_e not in d:
                d[p_e] = 0
            d[p_e] += 1
        return d

#print Solution().findAnagrams("abab", "ac")
# @lc code=end

