/*
 * @lc app=leetcode id=424 lang=cpp
 *
 * [424] Longest Repeating Character Replacement
 */

// @lc code=start
#include<iostream>
#include<vector>
#include<string>
using namespace std;

class Solution {
public:
    int characterReplacement(string s, int k) {
        int left = 0, right = 0,  maxCnt = 0;
        vector<int> win(26, 0);

        while(right < s.size()){
            ++win[s[right] - 'A'];
            maxCnt = max(maxCnt, win[s[right] - 'A']);
            if(right-left + 1 - maxCnt > k) {
                --win[s[left] - 'A'];
                left += 1;
            }
            right += 1;
        }
        return right - left;
    }
};

// int main() {
//     cout << Solution().characterReplacement("AABABBA", 2);
//     return 0;
// }
// @lc code=end

