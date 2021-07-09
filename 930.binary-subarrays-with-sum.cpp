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
        // int sum = 0;
        // map<int, int> cnt;
        // int ret = 0;
        // for(auto num: nums){
        //     cnt[sum] += 1;
        //     sum += num;
        //     ret += cnt[sum-goal];
        // }
        // return ret;
        int left1 = 0, left2 = left1, right=0;
        int sum = nums[right];
        int ret = 0;
        while(right < nums.size()){
            while(right < nums.size() && sum < goal){
            ++right;
            sum += nums[right]; 
            }
            if(right == nums.size()){
            return ret;
            }

            // 先找L1
            while(sum > goal && left1 < right){
            sum -= nums[left1];
            ++left1;
            }

            // 找L2
            left2 = left1;
            while(sum == goal && left2 < right && nums[left2] == 0){
            ++left2;
            }
            if(sum == goal){
            ret += left2 - left1 + 1;
            }
            
            right += 1;
            if(right < nums.size()){
            sum += nums[right];
            }

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

