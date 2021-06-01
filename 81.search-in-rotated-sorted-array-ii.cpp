/*
 * @lc app=leetcode id=81 lang=cpp
 *
 * [81] Search in Rotated Sorted Array II
 */

// @lc code=start
#include <iostream>
#include <vector>
#include<cassert>
using namespace std;

class Solution
{
public:
    bool search(vector<int> &nums, int target)
    {
        if (!nums.size())
        {
            return false;
        }
        
        int left = 0;
        int right = nums.size() - 1;
        int mid = 0;

        while (left < right)
        {
            while (left < right && nums[left] == nums[left + 1])
            {
                left += 1;
            }
            while (left < right && nums[right] == nums[right - 1])
            {
                right -= 1;
            }

            mid = (left + right) / 2;
            if (nums[mid] <= nums[left])
            {
                right = mid;
            }
            else
            {
                left = mid;
            }
        }

        if (mid > 0 && nums[mid] < nums[mid - 1])
        {
            mid = mid - 1;
        }

        left = 0;
        right = mid;
        while (left <= right)
        {
            int mid = (left + right) / 2;
            if (nums[mid] < target)
            {
                left = mid + 1;
            }
            else if (nums[mid] > target)
            {
                right = mid - 1;
            }
            else
            {
                return true;
            }
        }

        left = mid + 1;
        right = nums.size() - 1;

        while (left <= right)
        {
            int mid = (left + right) / 2;
            if (nums[mid] < target)
            {
                left = mid + 1;
            }
            else if (nums[mid] > target)
            {
                right = mid - 1;
            }
            else
            {
                return true;
            }
        }

        return false;
    }
};

int main()
{
    vector<int> nums = {2,5,6,0,0,1,2};
    
    assert(Solution().search(nums, 0) == true);
    
    nums = {1, 0, 1, 1, 1};
    assert(Solution().search(nums, 0) == true);


    nums = {1};
    assert(Solution().search(nums, 1) == true);

    nums = {4,5,6,7,0,1,2};
    assert(Solution().search(nums, 0) == true);
    
    nums = {15,16,19,20,25,1,3,4,5,7,10,14};
    assert(Solution().search(nums, 25) == true);
    return 0;
}
// @lc code=end
