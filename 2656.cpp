class Solution {
public:
    int maximizeSum(vector<int>& nums, int k) {
        auto num_vec = max_element(nums.begin(), nums.end());
        int num = *num_vec;
        return num * k + (k - 1)*k/2;
    }
};