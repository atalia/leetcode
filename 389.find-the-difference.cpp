/*
 * @lc app=leetcode id=389 lang=cpp
 *
 * [389] Find the Difference
 */

// @lc code=start
class Solution {
public:
    char findTheDifference(string s, string t) {
        vector<int> record(26, 0);
        for(int i = 0; i < s.size(); ++i){
            record[s[i] - 'a'] += 1;
        }

        for(int i = 0; i < t.size(); ++i){
          record[t[i] - 'a'] -= 1;
          if(record[t[i] - 'a'] < 0) {
            return t[i];
          }
        }
        return '0';
    }
};
// @lc code=end

