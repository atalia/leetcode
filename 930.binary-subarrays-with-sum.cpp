/*
 * @lc app=leetcode id=930 lang=cpp
 *
 * [930] Binary Subarrays With Sum
 */

#include<iostream>
#include<vector>
#include<map>
using namespace std;

// @lc code=start
class Solution {
public:
    int numSubarraysWithSum(vector<int>& nums, int goal) {
        int sum = 0;
        map<int, int> cnt;
        int ret = 0;
        for(auto num: nums){
            cnt[sum] += 1;
            sum += num;
            ret += cnt[sum-goal];
        }
        return ret;
    }
};

int main(){
    vector<int> nums = {0,0,0,0,0};
    cout << Solution().numSubarraysWithSum(nums, 0);
    return 0;
}
// @lc code=end

