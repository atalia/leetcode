#
# @lc app=leetcode id=322 lang=python
#
# [322] Coin Change
#

# @lc code=start
class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        if amount == 0:
            return 0
        vector = [amount+1 for _ in range(amount + 1)]
        vector_size = len(vector)
        for coin in coins:
            if coin < vector_size:
                vector[coin] = 1
        for idx in range(vector_size):
            if vector[idx] != amount:
                for coin in coins:
                    if idx + coin < vector_size:
                        vector[idx + coin] = min(vector[idx + coin], vector[idx]+1)
        return -1 if vector[-1] == amount+1 else vector[-1]

#print Solution().coinChange([2], 3)
# @lc code=end

