#
# @lc app=leetcode id=403 lang=python
#
# [403] Frog Jump
#
class Solution(object):
    def canCross(self, stones):
        """
        :type stones: List[int]
        :rtype: bool
        """
        size = len(stones)
        dp = [False for _ in range(len(stones))]
        dp[0] = True
        if stones[1] !=1:
            return False
        dp[1] = True
        canJump = dict()
        canJump[1] = set([0,1,2])
        for i in range(1, size):
            if stones[i] in canJump:
                for j in canJump[stones[i]]:
                    if j < 1:
                        continue
                    if stones[i]+j not in canJump:
                        canJump[stones[i]+j] = set()
                    canJump[stones[i]+j].add(j)
                    canJump[stones[i]+j].add(j-1)
                    canJump[stones[i]+j].add(j+1)
            if stones[-1] in canJump:
                break
        return stones[-1] in canJump

