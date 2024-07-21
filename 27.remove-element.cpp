/*
 * @lc app=leetcode id=27 lang=cpp
 *
 * [27] Remove Element
 */

// @lc code=start
#include<iostream>
#include<vector>

using namespace std;

class Solution {
public:
    int removeElement(vector<int>& nums, int val) {

        int start = 0;
        int current = 0;

        while(current < nums.size()){
            if(nums[current] != val){
                nums[start++] = nums[current++];
            } else {
                ++current;
            }
        }
        return start;
    }
};

// int main(){
//     vector<int> nums = {3,2,2,3};
//     int val = 2;
//     Solution s;
//     int result = s.removeElement(nums, val);
//     cout << result << endl;
// }
// @lc code=end

