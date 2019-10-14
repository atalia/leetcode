#
# @lc app=leetcode id=735 lang=python
#
# [735] Asteroid Collision
#
class Solution(object):
    def asteroidCollision(self, asteroids):
        """
        :type asteroids: List[int]
        :rtype: List[int]
        """
        stack = []
        for x in asteroids:
            alive = True
            while stack and stack[-1] > 0 and x < 0:
                if stack[-1] < -x:
                    stack.pop()
                elif stack[-1] > -x:
                    alive = False
                    break
                else:
                    stack.pop()
                    alive = False
                    break
            if alive:
                stack.append(x)
        return stack
