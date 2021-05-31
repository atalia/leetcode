/*
 * @lc app=leetcode id=477 lang=cpp
 *
 * [477] Total Hamming Distance
 */

// @lc code=start

#include <iostream>
#include <vector>
using namespace std;

class Solution
{
public:
    int totalHammingDistance(vector<int> &nums)
    {
        int result = 0;
        int bits[31] = {0};
        for (auto &num : nums)
        {
            for (int i = 0; i < 31 && num; ++i)
            {
                bits[i] += num & 0x1;
                num = num >> 1;
            }
        }
        int n = nums.size();
        for (auto &bit : bits)
        {
            result += bit * (n - bit);
        }
        return result;
    }
};

int main()
{
    vector<int> nums = {4,14,4,14};
    cout << Solution().totalHammingDistance(nums);
    return 0;
}
// @lc code=end
