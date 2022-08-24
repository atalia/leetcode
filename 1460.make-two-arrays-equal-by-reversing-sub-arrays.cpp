/*
 * @lc app=leetcode id=1460 lang=cpp
 *
 * [1460] Make Two Arrays Equal by Reversing Sub-arrays
 */

// @lc code=start
#include<iostream>
#include<vector>
#include<map>
using namespace std;

class Solution {
public:
    bool canBeEqual(vector<int>& target, vector<int>& arr) {
        map<int, int> map_target;
        map<int, int> map_arr;
        for(int i=0; i<target.size(); ++i) {
            if(map_target.cend() == map_target.find(target[i])) {
                map_target[target[i]] = 0;
            }
            map_target[target[i]] += 1;

            if (map_arr.cend() == map_arr.find(arr[i])) {
                map_arr[arr[i]] = 0;
            }
            map_arr[arr[i]] += 1;
        }

        for(auto it = map_target.begin(); it != map_target.end(); ++it){
            if(map_arr.cend() == map_arr.find(it->first)) {
                return false;
            }
            if(map_arr[it->first] != map_target[it->first]) {
                return false;
            }
        }
        return true;
    }
};
// @lc code=end

