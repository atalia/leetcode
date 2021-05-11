#include<iostream>
#include<vector>

using namespace std;

class Solution {
public:
    vector<int> decode(vector<int>& encoded) {
        int s = 0;
        for(int i=1;i<encoded.size()+2;++i){
            s ^= i;
        } 
        //cout << s <<endl;
        int t = 0;
        for(int i=1;i<encoded.size();i+=2){
            t ^=encoded[i];
        }
        //cout << t << endl;
        int first = s ^ t;
        vector<int> ret;
        ret.push_back(first);
        for(int i=0;i<encoded.size();++i){
            first ^= encoded[i];
            ret.push_back(first);
        }
        return ret;
    }
};

// void show(vector<int>& nums) {
//     cout << "show "<< endl;
//     for(auto i : nums){
//         cout << i << ", " ;
//     }
//     cout << endl;
// }

// int main(){
//     vector<int> encoded{3, 1};
//     //vector<int> encoded{6,5,4,6};
//     auto decode = Solution().decode(encoded);
//     show(decode);
//     return 0;
// }