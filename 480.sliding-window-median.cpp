/*
 * @lc app=leetcode id=480 lang=cpp
 *
 * [480] Sliding Window Median
 */

// @lc code=start
#include<vector>
#include<iostream>
#include<set>

using namespace std;

class Solution {
public:
    vector<double> medianSlidingWindow(vector<int>& nums, int k) {
        multiset<int> s;
        vector<double> ret;
        for(int i = 0; i < nums.size(); ++ i){
            s.insert(nums[i]);
            if (i >= k-1) {
                ret.push_back(getMedian(s));
                s.erase(s.find(nums[i-k+1]));
            }   
        }
        return ret;
    }

    static double getMedian(multiset<int> & s) {
        int k = s.size();
        int mid_right = k / 2;
        int mid_left = mid_right + k%2 - 1;
        int cur = 0;
        int left = 0, right = 0;
        for(auto i = s.begin(); i != s.end(); ++i){
            if(cur == mid_left) {
                left = *i;
                //cout << mid_left <<" left " << left << "  ";
            }
            if(cur == mid_right){
                right = *i;
                //cout << mid_right <<" right "<< right << endl;
                break;
            }
            cur += 1;
        }
        return (left * 1.0 + right * 1.0)/ 2.0;
    }    
};

int main(){
    vector<int> input = {7,0,3,9,9,9,1,7,2,3};
    auto vec = Solution().medianSlidingWindow(input, 6);
    for(auto &v: vec){
        cout << v << ", ";
    }
    cout << endl;
}
// @lc code=end

