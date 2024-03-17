/*
 * @lc app=leetcode id=202 lang=cpp
 *
 * [202] Happy Number
 */

// @lc code=start

#include<bits/stdc++.h>
#include<set>
using namespace std;

class Solution {
public:
    bool isHappy(int n) {
        static set<int> beSeed;
        if(n == 1) {
            return true;
        }
        if(beSeed.find(n) != beSeed.end()) {
            return false;
        }
        beSeed.insert(n);
        int m = 0;
        while(n){
            m += (n % 10) * (n % 10);
            n /= 10;
        }
        return isHappy(m);
    }
};

int main(int argc, char const *argv[]){
    if(argc == 2){
        int n = atoi(argv[1]);
        std::cout << n << std::endl;
        std::cout << Solution().isHappy(atoi(argv[1])) << std::endl;
    }
    
}
// @lc code=end

