#
# @lc app=leetcode id=207 lang=python
#
# [207] Course Schedule
#
# https://leetcode.com/problems/course-schedule/description/
#
# algorithms
# Medium (37.30%)
# Total Accepted:    204.4K
# Total Submissions: 546.7K
# Testcase Example:  '2\n[[1,0]]'
#
# There are a total of n courses you have to take, labeled from 0 to n-1.
# 
# Some courses may have prerequisites, for example to take course 0 you have to
# first take course 1, which is expressed as a pair: [0,1]
# 
# Given the total number of courses and a list of prerequisite pairs, is it
# possible for you to finish all courses?
# 
# Example 1:
# 
# 
# Input: 2, [[1,0]] 
# Output: true
# Explanation: There are a total of 2 courses to take. 
# To take course 1 you should have finished course 0. So it is possible.
# 
# Example 2:
# 
# 
# Input: 2, [[1,0],[0,1]]
# Output: false
# Explanation: There are a total of 2 courses to take. 
# To take course 1 you should have finished course 0, and to take course 0 you
# should
# also have finished course 1. So it is impossible.
# 
# 
# Note:
# 
# 
# The input prerequisites is a graph represented by a list of edges, not
# adjacency matrices. Read more about how a graph is represented.
# You may assume that there are no duplicate edges in the input prerequisites.
# 
# 
#
class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        self.visited = [0 for i in range(numCourses)]
        self.courses = [[0 for i in range(numCourses)] for j in range(numCourses)]
        self.flag = True
        for prerequisite in prerequisites:
            i, j = prerequisite
            self.courses[i][j] = 1
        for i in range(numCourses):
            self.dfs(i)
        return self.flag

    def dfs(self, s):
        if self.visited[s] == -1:
            return
        self.visited[s] = 1
        for i in range(len(self.visited)):
            if self.courses[s][i]:
                if not self.visited[i]:
                    self.dfs(i)
                elif self.visited[i] == 1:
                    self.flag = False
                    return
        self.visited[s] = -1

