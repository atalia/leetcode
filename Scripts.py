# coding:utf-8

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

if __name__ == '__main__':
    numCourses = 4
    prerequisites = [[1,0],[2,0],[2,1],[0,1]]
    print Solution().canFinish(numCourses, prerequisites)
