/*
 * @lc app=leetcode id=703 lang=cpp
 *
 * [703] Kth Largest Element in a Stream
 */

// @lc code=start
#include<vector>
#include<queue>
#include<iostream>
using namespace std;


class KthLargest {
    std::priority_queue<int> heap;
    int size;
public:
    KthLargest(int k, vector<int>& nums) {
        size = k;
        for(auto &num : nums){
            add(num);
        }
    }
    
    int add(int val) {
        if (heap.size() < size || heap.top() > -val){
            heap.push(-val);
            if (heap.size() > size) {
                heap.pop();
            }
        }   
        return -1 * heap.top();
    }
};

// int main(){
//     vector<int> nums =  {4,5,8,2};
//     auto kp = new KthLargest(3, nums);
//     cout << kp->add(3) << endl;
//     cout << kp->add(5) << endl;
//     cout << kp->add(10) << endl;
//     cout << kp->add(9) << endl;
//     cout << kp->add(4) << endl;
//     return 0;
// }

/**
 * Your KthLargest object will be instantiated and called as such:
 * KthLargest* obj = new KthLargest(k, nums);
 * int param_1 = obj->add(val);
 */
// @lc code=end

