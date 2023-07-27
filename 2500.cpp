#include<iostream>

#include<vector>
#include<algorithm>

using namespace std;

class Solution {
public:
    int deleteGreatestValue(vector<vector<int>>& grid) {
        for(auto& row: grid){
            sort(row.begin(), row.end());
        }
        int ret = 0;
        for(int i = 0; i< grid[0].size(); ++i){
            int m = 0;
            for(auto& row: grid) {
                m = m > row[i] ? m : row[i];
            }
            ret += m;
        }
        return ret;
    }
};