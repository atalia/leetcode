/*
 * @lc app=leetcode id=1921 lang=cpp
 *
 * [1921] Eliminate Maximum Number of Monsters
 */

// @lc code=start
class Solution {
public:
    int eliminateMaximum(vector<int>& dist, vector<int>& speed) {
        int n = dist.size();
        vector<int> arrivalTimes(n);

        for(int i = 0; i< n ; ++i) {
            arrivalTimes[i] = (dist[i] - 1) / speed[i] + 1;
        }
        sort(arrivalTimes.begin(), arrivalTimes.end());
        for(int i = 0; i< n; ++i) {
            if(arrivalTimes[i] <= i) {
                return i;
            }
        }
        return n;
    }
};
// @lc code=end

