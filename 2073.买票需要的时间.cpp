/*
 * @lc app=leetcode.cn id=2073 lang=cpp
 *
 * [2073] 买票需要的时间
 */

// @lc code=start
class Solution {
public:
    int timeRequiredToBuy(vector<int>& tickets, int k) {
        int curPos = 0;
        int ret = 0;
        int n = tickets.size();
        while(tickets[k] != 0){
            if(tickets[curPos % n ] == 0) {
                ++curPos;
                continue;
            }
            tickets[curPos % n] -= 1;
            ++ret;
            ++curPos;
        }
        return ret;
    }
};
// @lc code=end

