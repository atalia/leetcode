#
# @lc app=leetcode id=399 lang=python
#
# [399] Evaluate Division
#

# @lc code=start
class Solution(object):
    def calcEquation(self, equations, values, queries):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        """
        d = dict()
        idx = 0
        for e in equations:
            a, b = e
            if a not in d:
                d[a] = idx
                idx += 1
            if b not in d:
                d[b] = idx
                idx += 1
        elem_num = idx

        factor = [[0 for _ in xrange(elem_num)] for _ in xrange(elem_num)]
        for i in xrange(elem_num):
            factor[i][i] = 1.0

        for idx in xrange(len(equations)):
            a, b = equations[idx]
            val = values[idx]
            a_idx = d[a]
            b_idx = d[b]
            factor[a_idx][b_idx] = val
            factor[b_idx][a_idx] = 1 / val
        
        self.isVisited = set()
        
        def dfs(src, dst, val):
            if src == dst:
                return val
            if src in self.isVisited:
                return 0
            self.isVisited.add(src)
            for idx in xrange(elem_num):
                if src != idx and factor[src][idx] != 0:
                    r = dfs(idx, dst, val * factor[src][idx])
                    if r != 0:
                        break
            self.isVisited.remove(src)
            return r

        ret = []
        for query in queries:
            a, b = query
            if a not in d or b not in d:
                ret.append(-1.0)
                continue
            a_idx = d[a]
            b_idx = d[b]
            r = dfs(a_idx, b_idx, 1.0)
            if r != 0:
                factor[a_idx][b_idx] = r
                ret.append(r)
            else:
                ret.append(-1.0)
        return ret          
# @lc code=end

