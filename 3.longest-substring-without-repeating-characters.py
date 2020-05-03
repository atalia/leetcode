#
# @lc app=leetcode id=3 lang=python
#
# [3] Longest Substring Without Repeating Characters
#

# @lc code=start
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        left = 0
        right = 0
        characters = dict()
        max_length = 0
        while right < len(s):
            if s[right] not in characters or characters[s[right]] < left:
                characters[s[right]] = right
            else:
                left = characters[s[right]] + 1
                characters[s[right]] = right

            right += 1
            max_length = max(max_length, right-left)
            
        return max_length

print Solution().lengthOfLongestSubstring("au")
# @lc code=end

