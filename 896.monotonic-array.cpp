/*
 * @lc app=leetcode id=896 lang=cpp
 *
 * [896] Monotonic Array
 */

// @lc code=start
#include<iostream>
#include<vector>

using namespace std;
class Solution {
public:
    bool isMonotonic(vector<int>& A) {
        int flag = 0;
        for(int i = 1; i < A.size();i++){
            int diff = A[i] - A[i-1];
            if (diff != 0){
                if(flag == 0){
                    flag = abs(diff) / diff;
                    continue;
                }
                if(flag != abs(diff)/diff){
                    return false;
                }
            }
        }
        return true;
    }
};

// int main(){
//     vector<int> A = {6,5,4,4};
//     cout << Solution().isMonotonic(A) << endl;
//     return 0;
// }

// @lc code=end

