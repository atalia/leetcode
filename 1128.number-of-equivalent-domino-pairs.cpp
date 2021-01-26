/*
 * @lc app=leetcode id=1128 lang=cpp
 *
 * [1128] Number of Equivalent Domino Pairs
 */

// @lc code=start
#include<iostream>
#include<vector>
using namespace std;

class Solution {
public:
    int numEquivDominoPairs(vector<vector<int>>& dominoes) {
        vector<int> rec(100, 0);
        int cnt = 0, r = 0;
        for (auto &domino : dominoes) {
            r = domino[0] < domino[1] ? (domino[0] * 10 + domino[1]) : (domino[1] * 10 + domino[0]);
            cnt += rec[r]; 
            rec[r] += 1;
        }
        return cnt;
    }
};
// @lc code=end

