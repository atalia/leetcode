#
# @lc app=leetcode id=785 lang=python
#
# [785] Is Graph Bipartite?
#
class Solution(object):
    def isBipartite(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: bool
        """
        node_size = len(graph)
        self.graph = graph
        self.color = [-1 for i in xrange(node_size)]
        self._set = [i for i in xrange(node_size)]
        self.visited = [0 for i in xrange(node_size)]
        while self._set:
            if not self._dfs(self._set[0], 0):
                return False
        return True


    def _dfs(self, i, val):
        i in self._set and self._set.remove(i)
        if self.visited[i]:
            return True
        self.visited[i] = 1
        if self.color[i] == val:
            return True
        elif self.color[i] == 1-val:
            return False
        else:
            self.color[i] = val
        for node in self.graph[i]:
            if not self._dfs(node, 1 - val):
                return False
        self.visited[i] = 0
        return True
