/*
 * @lc app=leetcode id=88 lang=cpp
 *
 * [88] Merge Sorted Array
 */

// @lc code=start
#include<iostream>
#include<vector>
using namespace std;

class Solution {
public:
    void merge(vector<int>& nums1, int m, vector<int>& nums2, int n) {
        for(int i=m-1; i>=0;--i){
            nums1[i+n] = nums1[i];
        }
        int start1 = 0, start2 = 0;
        while(start1 < m && start2 < n){
            if(nums1[start1+n] < nums2[start2]){
                nums1[start1+start2] = nums1[start1+n];
                ++start1;
            }else{
                nums1[start1+start2] = nums2[start2];
                ++start2;
            }
        }
        while(start2 < n){
            nums1[start1 + start2] = nums2[start2];
            ++start2;
        }
    }
};

// int main(){
//     vector<int> nums1 = {1};
//     vector<int> nums2 = {0};
//     Solution().merge(nums1, 0, nums2, 0);
//     for(auto &num: nums1){
//         cout << num << " ";
//     }
//     cout << endl;
//     return 0;
// }
// @lc code=end

