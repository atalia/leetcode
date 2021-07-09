/*
 * @lc app=leetcode id=122 lang=cpp
 *
 * [122] Best Time to Buy and Sell Stock II
 */

// @lc code=start
#include<iostream>
#include<vector>
using namespace std;

class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int start = -1;
        int day = 1;
        int profit = 0;
        while(day < prices.size()){
            while(day < prices.size() && prices[day] <= prices[day-1]){
                ++day;
            }
            start = day - 1;
            while(day < prices.size() && prices[day] > prices[day-1]){
                ++day;
            }
            profit += prices[day-1] - prices[start];
            start = -1;
        }
        return profit;
    }
};

// int main(){
//     vector<int> nums = {3,3};
//     cout << Solution().maxProfit(nums);
//     return 0;
// }
// @lc code=end

