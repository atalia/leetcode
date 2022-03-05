/*
 * @lc app=leetcode id=799 lang=cpp
 *
 * [799] Champagne Tower
 */

// @lc code=start
#include <math.h>
#include <vector>
#include <iostream>
using namespace std;

// template<typename T>
// void showVector(const vector<T>& vec){
//     for(auto const &e : vec){
//         cout << e << " ";
//     }
//     cout << endl;
// }

class Solution {
public:
    double champagneTower(int poured, int query_row, int query_glass) {
        vector<vector<double>> glasses(101, vector<double>(101, 0));
        glasses[0][0] = poured;
        
        for(int i = 0; i < query_row + 1; ++i){
            bool end = true;
            for(int j = 0; j <= i; ++j){
                if(glasses[i][j] > 1) {
                    double overflow = glasses[i][j] - 1;
                    glasses[i+1][j] += overflow/2;
                    glasses[i+1][j+1] += overflow/2;
                    glasses[i][j] = 1;
                    end = false;
                }
            }
            if(end) {
                break;
            }
        }
        return glasses[query_row][query_glass];
    }
};

// int main(){
//     double a = Solution().champagneTower(25,6,1);
//     // double a = Solution().champagneTower(100000009,33,17);
//     cout << a << endl;
//     return 0;
// }
// @lc code=end

