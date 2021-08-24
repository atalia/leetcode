/*
 * @lc app=leetcode id=1646 lang=cpp
 *
 * [1646] Get Maximum in Generated Array
 */

// @lc code=start
#include<iostream>
#include<vector>
using namespace std;
class Solution {
public:
    int getMaximumGenerated(int n) {
        if(n < 2){
            return n;
        }
        vector<int> ret(n+1, 0);
        ret[1] = 1;
        int cur_max = 1;
        int idx = 2;
        while (idx <= n)
        {
            if (idx & 0x01)
            {
                ret[idx] = ret[idx/2] + ret[idx/2+1];
            }else{
                ret[idx] = ret[idx/2];
            }
            cur_max = cur_max > ret[idx] ? cur_max : ret[idx];
            idx += 1;
        }
        return cur_max;
    }
};

// int main(){

//     cout << Solution().getMaximumGenerated(100) << endl;
//     cout << Solution().getMaximumGenerated(2) << endl;
//     cout << Solution().getMaximumGenerated(3) << endl;
//     return 0;
// }
// @lc code=end

