/*
 * @lc app=leetcode id=788 lang=cpp
 *
 * [788] Rotated Digits
 */

// @lc code=start

#include<iostream>
#include<vector>
using namespace std;
class Solution {
public:

    int rotatedDigits(int n) {
        int res = 0;
        vector<int> dp(n+1);
        for(int i=0;i<=n;++i){
            if(i<10){
                if(i==2 || i==5 || i==6|| i==9) {
                    dp[i] = 2;
                    res += 1;
                }else if (i==0 || i==1 ||i==8){
                    dp[i] = 1;
                }
            }else{
                int a = dp[i / 10], b = dp[i % 10];
                if ( a >= 1 && b >= 1) {
                    dp[i] = 2;
                    res += 1;
                }else if (a == 1 && b == 1){
                    dp[i] = 1;
                }
            }
        }
        return res;
    }
};

// int main(){
//     int b ;
//     while (true){
//         cin >> b;
//         cout << Solution().rotatedDigits(b) << endl;
//     }
//     return 0;
// }
// @lc code=end

