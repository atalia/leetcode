/*
 * @lc app=leetcode id=839 lang=cpp
 *
 * [839] Similar String Groups
 */

// @lc code=start
#include<iostream>
#include<vector>
#include<string>
using namespace std;

class Solution {
    vector<int> root;
public:
    int numSimilarGroups(vector<string>& strs) {
         root = vector<int>(strs.size(), 0);
         int cnt = strs.size();
         for (int i = 0; i < root.size() ; ++i) {
             root[i] = i;
         }

         for ( int i = 0; i < strs.size(); ++i) {
             for (int j = i + 1 ; j < strs.size(); ++j ){
                 int r_i = find(i);
                 int r_j = find(j);
                 if(r_i == r_j){
                     continue;
                 }

                 if(isSimilar(strs[i], strs[j])){
                     //cout <<"similar " << i << ", " << j << endl;
                     root[r_j] = r_i;
                     cnt -= 1;
                 }
             }
         }
        // for(auto &x : root){
        //     cout << x << " ";
        // }
        //cout << endl;
        return cnt;
    }

    int find(int x) {
        int parent = root[x];
        while(parent != root[parent]){
            parent = root[parent];
        }
        while(x != parent) {
            int tmp = root[x];
            root[x] = parent;
            x = tmp;
        }
        return parent;
    }

    bool isSimilar(const string& lhs, const string& rhs) {
        int diff = 0;
        for (int i = 0 ; i < lhs.size(); ++i) {
            if(lhs[i] != rhs[i]) {
                diff += 1;
                if(diff > 2) {
                    return false;
                }
            }
        }
        return true;
    }
};


int main(){
    vector<string> strs = {"tars","rats","arts","star"};
    //vector<string> strs = {"omv","ovm"};
    //vector<string> strs = {"qihcochwmglyiggvsqqfgjjxu","gcgqxiysqfqugmjgwclhjhovi","gjhoggxvcqlcsyifmqgqujwhi","wqoijxciuqlyghcvjhgsqfmgg","qshcoghwmglygqgviiqfjcjxu","jgcxqfqhuyimjglgihvcqsgow","qshcoghwmggylqgviiqfjcjxu","wcoijxqiuqlyghcvjhgsqgmgf","qshcoghwmglyiqgvigqfjcjxu","qgsjggjuiyihlqcxfovchqmwg","wcoijxjiuqlyghcvqhgsqgmgf","sijgumvhqwqioclcggxgyhfjq","lhogcgfqqihjuqsyicxgwmvgj","ijhoggxvcqlcsygfmqgqujwhi","qshcojhwmglyiqgvigqfgcjxu","wcoijxqiuqlyghcvjhgsqfmgg","qshcojhwmglyiggviqqfgcjxu","lhogcgqqfihjuqsyicxgwmvgj","xscjjyfiuglqigmgqwqghcvho","lhggcgfqqihjuqsyicxgwmvoj","lhgocgfqqihjuqsyicxgwmvgj","qihcojhwmglyiggvsqqfgcjxu","ojjycmqshgglwicfqguxvihgq","sijvumghqwqioclcggxgyhfjq","gglhhifwvqgqcoyumcgjjisqx"};
    //cout << strs.size() << std::endl;
    cout << Solution().numSimilarGroups(strs) << endl;
    return 0;
}
// @lc code=end