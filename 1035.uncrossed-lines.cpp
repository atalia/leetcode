/*
 * @lc app=leetcode id=1035 lang=cpp
 *
 * [1035] Uncrossed Lines
 */

// @lc code=start
#include<iostream>
#include<vector>
#include<algorithm>
using namespace std;

    
class Solution {
public:
    int maxUncrossedLines(vector<int>& nums1, vector<int>& nums2) {
        vector<int> dp (nums1.size() + 1, 0);
        int before = 0, tmp = 0;
        for(int j = 0; j < nums2.size(); ++j){
            before = 0;
            for(int i = 1; i < nums1.size()+1; ++i){
                tmp = dp[i];
                dp[i] = max(before + (nums1[i-1] == nums2[j]), dp[i]);
                dp[i] = max(dp[i], dp[i-1]);
                before = tmp; 
            
            }
        }

        return dp[nums1.size()];    
    }
};

int main(){
    vector<int> num1 {2,5,1,2,5};
    vector<int> num2 {10,5,2,1,5,2};
    cout << Solution().maxUncrossedLines(num1, num2) << endl;
    return 0;
}
// @lc code=end

