/*
 * @lc app=leetcode id=309 lang=cpp
 *
 * [309] Best Time to Buy and Sell Stock with Cooldown
 */

// @lc code=start
#include <iostream>
#include <vector>

using namespace std;
class Solution
{
public:
    int maxProfit(vector<int> &prices)
    {
        vector<vector<int> > dp(prices.size(), vector<int>(3, 0));
        dp[0][1] = -prices[0];
        for (int i = 1; i < dp.size(); ++i)
        {
            // 0 没有
            // 1 有
            // 2 冷冻
            dp[i][0] = max(dp[i-1][2], dp[i-1][0]);
            dp[i][1] = max(dp[i-1][1], dp[i-1][0] - prices[i]);
            dp[i][2] = dp[i-1][1] + prices[i];
        }
        return max(dp[dp.size()-1][0], dp[dp.size()-1][2]);
    }
};


int main()
{
    vector<int> prices={1,2,3,0,2};
    cout << Solution().maxProfit(prices)<<endl;
    return 0;
}
// @lc code=end
