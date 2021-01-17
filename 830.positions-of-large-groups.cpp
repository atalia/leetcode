/*
 * @lc app=leetcode id=830 lang=cpp
 *
 * [830] Positions of Large Groups
 */

// @lc code=start
#include<iostream>
#include<string>
#include<vector>
using namespace std;


class Solution {
public:
    vector<vector<int> > largeGroupPositions(string s) {
        vector<vector<int>> ret;
        for(int i = 0; i<s.length();){
            int j = i+1 ;
            while(j < s.size() && s[i] == s[j]){
                ++j;
            }
            if(j - i > 2){
                vector<int> cap;
                cap.push_back(i);
                cap.push_back(j-1);
                ret.push_back(cap);
            }
            i = j;
        }
        return ret;
    }
};

int main(){
    vector<vector<int> > ret =  Solution().largeGroupPositions("aba");
    for (int i = 0; i< ret.size(); ++i){
        cout << "[" << ret[i][0] << ", " <<ret[i][1] << "], ";
    }
    return 0;
}

// @lc code=end

