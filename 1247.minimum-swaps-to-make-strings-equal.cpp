/*
 * @lc app=leetcode id=1247 lang=cpp
 *
 * [1247] Minimum Swaps to Make Strings Equal
 */

#include<iostream>
#include<string>
#include<vector>

using namespace std;

// @lc code=start
class Solution {
public:
    int minimumSwap(string s1, string s2) {
         int cnt[2]{};
        for (int i = 0, n = s1.length(); i < n; ++i)
            if (s1[i] != s2[i])
                ++cnt[s1[i] % 2]; // x 和 y ASCII 值的二进制最低位不同
        int d = cnt[0] + cnt[1];
        return d % 2 != 0 ? -1 : d / 2 + cnt[0] % 2;
    }
};

// @lc code=end
