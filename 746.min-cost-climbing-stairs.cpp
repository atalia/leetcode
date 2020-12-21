/*
 * @lc app=leetcode id=746 lang=cpp
 *
 * [746] Min Cost Climbing Stairs
 */

// @lc code=start
#include <iostream>
#include<vector>
using namespace std;

class Solution {
public:
    int minCostClimbingStairs(vector<int>& cost) {
        vector<int> dp(cost.size());
        dp[0] = cost[0];
        dp[1] = cost[1];
        for(int i = 2;i < cost.size(); ++i){
            dp[i] = min(dp[i-1], dp[i-2])+cost[i];
        }
        for(int i=0;i<cost.size();++i){
            cout<<dp[i] << " ";
        }
        cout << endl;
        return min(dp[dp.size()-1], dp[dp.size()-2]);
    }
};

// int main(){
//     vector<int> cost = {1, 100, 1, 1, 1, 100, 1, 1, 100, 1};
//     cout << Solution().minCostClimbingStairs(cost) << endl;  
//     return 0;

// }
// @lc code=end

