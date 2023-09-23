/*
 * @lc app=leetcode id=2418 lang=cpp
 *
 * [2418] Sort the People
 */

// @lc code=start
class Solution {
public:
    vector<string> sortPeople(vector<string>& names, vector<int>& heights) {
        map<int, string> tmp;
        for(int i=0; i< names.size(); ++i){
            tmp[heights[i]] = names[i];
        }
        vector<string> ret;
        for(auto it =  tmp.crbegin(); it != tmp.crend(); ++it) {
            ret.push_back(it->second);
        }
        return ret;
    }
};
// @lc code=end

