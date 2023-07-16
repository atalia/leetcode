/*
 * @lc app=leetcode id=26 lang=cpp
 *
 * [26] Remove Duplicates from Sorted Array
 */

// #include <vector>
// #include <iostream>
// using namespace std;
// @lc code=start
class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        int left = 0, right=1;
        int ret = 1;
        while(right < nums.size()) {
            if(nums[right] != nums[right-1]){
                ++left;
                nums[left] = nums[right];
                ++ret;
            }
            ++right;
        }
        return ret;
    }
};

// int main() {
//     vector<int> v{0};
//     std::cout << Solution().removeDuplicates(v) << std::endl;
//     for(const auto& e: v){
//         std:: cout << e << " ";
//     }
//     return 0;
// }

// @lc code=end

