#coding:utf-8
# @lc app=leetcode.cn id=210 lang=python
#
# [210] 课程表 II
#

# @lc code=start
class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        node_out = dict((i, []) for i in range(numCourses))
        node_in = dict((i, 0) for i in range(numCourses))
        queue = list(idx for idx in range(numCourses))
        
        for prerequisite in prerequisites:
            i, o = prerequisite
            node_out[o].append(i)
            node_in[i] += 1
            if i in queue:
                queue.remove(i)
        
        if not queue:
            return []

        result = []

        while queue:
            node = queue.pop(0)
            result.append(node)
    
            for n in node_out[node]:
                node_in[n] -= 1
                if not node_in[n]:
                    queue.append(n)
            node_out[node] = []
        
        if len(result) == numCourses:
            return result
        else:
            return []

# @lc code=end

