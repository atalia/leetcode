/*
 * @lc app=leetcode id=944 lang=cpp
 *
 * [944] Delete Columns to Make Sorted
 */

// @lc code=start
// #include <iostream>
// #include <vector>
// #include <string>
// using namespace std;


class Solution {
public:
    int minDeletionSize(vector<string>& strs) {
        if(strs.size() < 2) {
            return 0;
        }

        int count = 0;
        for(int i = 0 ;i < strs[0].size() ;++i){
            for(int j=1; j < strs.size(); ++j) {
                if(strs[j][i] < strs[j-1][i]){
                    ++count;
                    break;
                }
            }
        }
        return count;
    }
};
// @lc code=end

// int main(){
//     vector<string> input{"zyx","wvu","tsr"};
//     Solution s;
//     cout << s.minDeletionSize(input) << endl;

// }