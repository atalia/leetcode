/*
 * @lc app=leetcode id=264 lang=cpp
 *
 * [264] Ugly Number II
 */

// @lc code=start
class Solution {
public:
    int nthUglyNumber(int n) {
        vector<int> ret(n+1, 0);
        ret[1] = 1;
        int p2=1,  p3=1, p5 = 1;
        int num = 0;
        for(size_t i = 2; i < ret.size(); ++i){
            ret[i] = min(ret[p2] * 2, min(ret[p3] * 3, ret[p5] * 5));
            if(ret[i] == ret[p2] * 2){
                p2 += 1;
            }
            if (ret[i] == ret[p3] * 3)
            {
                p3 += 1;
            }
            if (ret[i] == ret[p5] * 5){
                p5 += 1;
            }   
        }
        return ret[n];
    }
};

// @lc code=end

